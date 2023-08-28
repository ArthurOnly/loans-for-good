
# Loans project

>O sistema permite que usuários não cadastrados solicitem um empréstimo  que pode ser avaliado por um usuário acessando o sistema de administração.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Você instalou a versão mais recente do `docker` e `docker compose`
* Você tem uma máquina `<Windows / Linux / Mac>`. 

## 🚀 Instalando loans_project

Para instalar o loans_project, siga estas etapas:
1. Clonando repositório
```
git clone https://github.com/ArthurOnly/loans-for-good
```
2. Acessando a pasta
```
cd loans-for-good
```
3. Criando arquivo local_settings
```
cp backend/loans_project/local_settings_sample.py backend/loans_project/local_settings.py
```
4. Criando containers
```
docker compose up
```
5. Criando dados iniciais
```
docker compose exec django python manage.py seed_loans
```
6. Feito isso basta acessar [http://localhost:8000/admin](http://localhost:8000/admin) e ver se tudo deu certo.

## ☕ Usando loans_project

Para usar loans_project, siga estas etapas:
* Para executar o sistema
```
docker compose up
```
* Para executar os testes
```
docker compose exec django python manage.py test
```

### Uso geral
* Para acessar a interface de administração acesse http://localhost:8000/admin e use o login `admin` e senha `admin`
* Para acessar o formulário acesse http://localhost:5173/
* Cada Questão aparecerá no formulário do cliente se tiver a flag `active` como `True`


## 📫 Contribuindo para loans_project

Para contribuir com loans_project, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://media.licdn.com/dms/image/C4D03AQEUm_hTUDpG3A/profile-displayphoto-shrink_200_200/0/1659916193136?e=1698883200&v=beta&t=3CDNJPZqvXwL5LZnGezFDLEsC1n9Vw4ZhVQ7xitJ7kw" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Arthur Paiva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
