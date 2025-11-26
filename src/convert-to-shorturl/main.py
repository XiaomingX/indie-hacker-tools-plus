import os
import secrets
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from supabase import create_client
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化Flask应用
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', secrets.token_hex(32))

# 初始化Supabase客户端
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

def generate_random_code(length=6):
    """生成随机短码"""
    return secrets.token_urlsafe(length)[:length]

def validate_custom_code(code):
    """验证自定义短码是否合法"""
    return code.isalnum() and 3 <= len(code) <= 20

def normalize_url(url):
    """标准化URL格式"""
    url = url.strip()
    if not url:
        return None
    
    # 确保URL以http://或https://开头
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    return url.lower()

def is_valid_url(url):
    """简单验证URL格式（替代validators库）"""
    if not url:
        return False
    # 检查基本格式，实际应用可能需要更复杂的验证
    return '.' in url.split('//')[-1].split('/')[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 处理表单提交
        original_url = normalize_url(request.form.get('url'))
        custom_code = request.form.get('custom_code', '').strip()

        # 验证URL
        if not original_url or not is_valid_url(original_url):
            flash('请输入有效的URL（例如：https://example.com）', 'error')
            return redirect(url_for('index'))

        # 处理自定义短码
        if custom_code:
            if not validate_custom_code(custom_code):
                flash('自定义短码必须是3-20位字母或数字', 'error')
                return redirect(url_for('index'))
            short_code = custom_code
        else:
            # 生成随机短码并确保唯一
            short_code = generate_random_code()
            attempts = 0
            while attempts < 5:
                existing = supabase.table('urls').select('short_code').eq('short_code', short_code).execute()
                if not existing.data:
                    break
                short_code = generate_random_code()
                attempts += 1
            else:
                flash('无法生成唯一短码，请重试', 'error')
                return redirect(url_for('index'))

        # 保存到数据库
        try:
            response = supabase.table('urls').insert({
                'original_url': original_url,
                'short_code': short_code,
                'created_at': datetime.utcnow().isoformat(),
                'clicks': 0
            }).execute()

            if response.data:
                short_url = f"{request.host_url.rstrip('/')}/{short_code}"
                return render_template('index.html', 
                                       short_url=short_url,
                                       original_url=original_url)

        except Exception as e:
            print(f"数据库错误: {str(e)}")
            if 'duplicate key' in str(e).lower():
                flash('该自定义短码已被使用，请尝试其他', 'error')
            else:
                flash('发生错误，请重试', 'error')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/<short_code>')
def redirect_url(short_code):
    try:
        # 查询原始URL
        response = supabase.table('urls') \
            .select('original_url') \
            .eq('short_code', short_code) \
            .maybe_single() \
            .execute()

        if response.data and 'original_url' in response.data:
            original_url = response.data['original_url']
            
            # 确保URL有协议前缀
            if not original_url.startswith(('http://', 'https://')):
                original_url = f'https://{original_url}'

            # 更新点击计数
            try:
                supabase.table('urls') \
                    .update({'clicks': supabase.rpc('increment')}) \
                    .eq('short_code', short_code) \
                    .execute()
            except Exception as e:
                print(f"更新点击数失败: {str(e)}")

            return redirect(original_url, code=302)

        # 未找到短码
        flash('短链接不存在', 'error')
        return render_template('error.html', error="URL不存在"), 404

    except Exception as e:
        print(f"重定向错误: {str(e)}")
        flash('重定向失败', 'error')
        return render_template('error.html', error="重定向失败"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)