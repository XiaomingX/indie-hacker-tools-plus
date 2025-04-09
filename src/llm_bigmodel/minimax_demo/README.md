curl --location "https://api.minimaxi.chat/v1/text/chatcompletion_v2" \
--header "Content-Type: application/json" \
--header "Authorization: Bearer $MiniMax_API_KEY" \
--data '{
    "model":"abab6.5s-chat",
    "messages":[
      {
        "role":"system",
        "name":"MM Intelligent Assistant", # Optional
        "content":"MM Intelligent Assistant is a large language model that is self-developed by MiniMax and does not call the interface of other products. "
      },
      {
        "role":"user",
        "name":"user", # Optional
        "content":"hello”"
      }
    ]
  }'
  