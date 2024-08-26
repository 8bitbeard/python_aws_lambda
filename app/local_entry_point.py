from lambda_function import lambda_handler

input_event = {
    "payload": {
        "topic": "abcd",
        "partition": 1,
        "offset": 1,
        "key": "kafka",
        "value": "{"
                 "\"nome_canal_requisicao\": \"wiltsou|987654|7a9a1203-5f52-4cc1-90cf-981ed6fbb301\","
                 "\"data_vencimento_anterior\": \"01/01/01\","
                 "\"data_vencimento_atual\": \"01/01/01\","
                 "\"data_troca_vencimento\": \"01/01/01\""
                 "}",
        "headers": [{"abvc": "abc"}],
        "timestamp": 12345
    }
}

r = lambda_handler(input_event, None)

print(r)
