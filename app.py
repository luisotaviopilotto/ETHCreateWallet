import gradio as gr
from mnemonic import Mnemonic
from eth_account import Account
from eth_keys import keys

Account.enable_unaudited_hdwallet_features()

def gerar_carteira(num_words, passphrase, deriv_path, lang):
  acct, mnemonic_phrase = Account.create_with_mnemonic(passphrase, int(num_words), lang, deriv_path)
  private_key = keys.PrivateKey(acct.key)
  public_key = private_key.public_key
  compressed_public_key = public_key.to_compressed_bytes().hex()

  return f"""
  Carteira ETH criada com sucesso!

  Chave Mnemônica: {mnemonic_phrase}
  Carteira ETH: {acct.address}
  Chave Privada: {private_key.to_hex()}
  Chave Pública: 0x{compressed_public_key}
  """

mnemo = Mnemonic("english")
available_languages = mnemo.list_languages()
available_languages.remove("portuguese") # não funciona
available_languages.remove("russian") # não funciona
available_languages.remove("turkish") # não funciona

iface = gr.Interface(
  fn=gerar_carteira,
  inputs=[
    gr.Number(label="Mnemonic Number: 12, 15, 18, 21 ou 24", value="12"), 
    gr.Textbox(label="Passphrase"),
    gr.Textbox(label="Derivation Path", value="m/44'/60'/0'/0/0"),
    gr.Dropdown(label="Language", choices=available_languages, value="english")
  ],
  outputs="text",
  title="Gerador de Carteira Ethereum",
  description="Este aplicativo gera uma carteira Ethereum com chave mnemônica, endereço, chave privada e chave pública."
)

iface.launch()