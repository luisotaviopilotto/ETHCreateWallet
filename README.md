# Gerador de Carteira Ethereum

Este é um aplicativo simples para gerar uma carteira Ethereum com chave mnemônica, endereço, chave privada e chave pública.

## Como usar

1. Certifique-se de ter todas as dependências instaladas. Você pode instalá-las usando o seguinte comando:
   
```
pip install -r requirements.txt
``` 
2. Execute o arquivo `gerador_carteira.py` usando o Python:

```
python gerador_carteira.py
```

3. O aplicativo será iniciado e você será solicitado a inserir as seguintes informações:
- Número de palavras da Mnemônica: 12, 15, 18, 21 ou 24.
- Frase secreta (passphrase).
- Caminho de derivação (Derivation Path).
- Idioma da Mnemônica: Escolha entre os idiomas disponíveis.

4. Após inserir as informações solicitadas, a carteira Ethereum será gerada e os seguintes detalhes serão exibidos:
- Chave Mnemônica.
- Endereço da Carteira Ethereum.
- Chave Privada.
- Chave Pública.

## Dependências

Certifique-se de ter as seguintes bibliotecas instaladas:
- gradio
- mnemonic
- eth_account
- eth_keys

Você pode instalá-las manualmente usando o seguinte comando:

```
pip install gradio mnemonic eth_account eth_keys
```

## Nota

- Este aplicativo remove os idiomas "português", "russo" e "turco" da lista de idiomas disponíveis, pois esses idiomas atualmente não estão funcionando corretamente com a biblioteca `mnemonic`.
