import boto3
import json

# Cria o cliente Bedrock Runtime
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

print("=== Chat com Amazon Titan (Geração de Texto) ===")
print("Digite 'sair' para encerrar.\n")

# Loop de interação
while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até logo!")
        break

    # Cria o corpo da requisição com o prompt do usuário
    body = {
        "inputText": pergunta,
        "textGenerationConfig": {
            "temperature": 0.7,   # controla a criatividade
            "maxTokenCount": 200, # tamanho máximo da resposta
            "stopSequences": []   # pode definir palavras que interrompem a resposta
        }
    }

    # Envia o prompt para o modelo Titan
    response = bedrock.invoke_model(
        modelId="amazon.titan-text-express-v1",
        body=json.dumps(body)
    )

    # Lê e formata a resposta
    response_body = json.loads(response["body"].read())
    resposta = response_body["results"][0]["outputText"]

    print(f"Bedrock: {resposta}\n")
