# Python Password Manager 

Este é um gerenciador de senhas simples e seguro desenvolvido em Python. O projeto utiliza criptografia simétrica para garantir que apenas quem possui a chave correta possa acessar as senhas armazenadas.

## Funcionalidades
**Geração de Chaves**: Cria chaves de criptografia exclusivas (.key).

**Armazenamento Criptografado**: As senhas são salvas em um arquivo de texto, mas seus valores permanecem ilegíveis sem a chave.

**Gestão de Identificadores**: Associa senhas a sites ou serviços específicos (ex: *Facebook, Email*).

**Segurança com Fernet**: Utiliza o algoritmo de criptografia simétrica da biblioteca *cryptography*.

## Tecnologias e Bibliotecas
**Python 3.x** 

*Cryptography*: Biblioteca principal para cifrar e decifrar os dados.

**Instalação**: pip install cryptography

### Como Executar
1. **Preparação**
Certifique-se de ter a biblioteca necessária instalada:

Bash

pip install cryptography
2. **Rodando o Script**
Execute o arquivo principal:

Bash

python main.py
3. **Fluxo de Uso**
Ao abrir o menu, siga a ordem lógica para garantir o funcionamento:

Opção 1: Crie uma nova chave (ex: minha_chave.key).

Opção 3: Crie um novo arquivo de senhas (ex: senhas.txt).

Opção 5: Adicione novas senhas informando o site e a senha desejada.

Opção 6: Recupere uma senha existente informando o nome do site.

Nota: Se você fechar o programa e abri-lo novamente, lembre-se de usar a Opção 2 **(Carregar Chave)** e a Opção 4 **(Carregar Arquivo de Senhas)** antes de tentar buscar qualquer informação.

## Estrutura do Código
O projeto é estruturado em uma classe principal chamada PasswordManager, que contém métodos para:

*create_key()*: Gera e salva uma chave em disco.

*load_key()*: Carrega uma chave existente para a memória.

*add_password()*: Criptografa e anexa uma nova senha ao arquivo.

*get_password()*: Decriptografa e exibe a senha solicitada.

## Aviso de Segurança
Este projeto foi criado para fins educacionais. Embora utilize criptografia forte (AES), o armazenamento da chave no mesmo ambiente que o arquivo de senhas não é recomendado para segurança de nível profissional.

