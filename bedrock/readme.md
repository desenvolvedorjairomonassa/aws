
Folder about generative

Notebooks with NLP functionality are available in Bedrock: Mistral, Titan, Cohere Command, and Meta Llama.

To use the boto3 SDK:

The input format for the request body and response will vary depending on the chosen model.
Simply use the invoke_model function provided by the SDK.

For streaming:

If you want to use streaming (i.e., receive the output in chunks as it's generated rather than waiting for the full response), this is possible using invoke_model_with_response_stream

Parametros

Top k - corte de quantide de resultado que irá retornar, assim sendo, é definido por um numero inteiro

Top P - corte de procetagem agregadas que vai trazer, ele tem como entrada um floar

Temperatura, que vai de 0 a 1, quanto mais perto de 0 vai retornar a palavra que estiver mais alta probabilidade

max_tokens = máximo numero de token de respota total
