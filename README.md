# quante

_Quanté?_ é um aplicativo mobile que permite aos usuários pesquisar preços de produtos e serviços. 

Será desenvolvido como um trabalho para a disciplina de [Engenharia de Software](https://github.com/aserg-ufmg/CursoEngenhariaSoftware) (2020/1).

## Equipe de Desenvolvedores

- [Guilherme Miranda](https://github.com/guilhermealbm)
- [Lorena Leão](https://github.com/lorenaleao)
- [Matheus Guilherme Veloso](https://github.com/MaMiotto)
- [Raphael Augusto](https://github.com/Maharal)
- [Tomaz Gomes](https://github.com/tomaz1502)

## Ferramentas de organização do processo de desenvolvimento

- _**Trello**_: para que possamos acompanhar a evolução da implementação das histórias, criamos um quadro _Scrum_ (ou _Scrum Board_) no _Trello_ com as colunas _To Do_, _In Progress_, _To Verify_ e _Done_.
- _**GitHub Flow**_: decidimos adotar o [_GitHub Flow_](https://guides.github.com/introduction/flow/) como o nosso fluxo de trabalho. Seus princípios são os seguintes:

  > - Anything in the master branch is deployable
  > - To work on something new, create a descriptively named branch off of master (ie: new-oauth2-scopes)
  > - Commit to that branch locally and regularly push your work to the same named branch on the server
  > - When you need feedback or help, or you think the branch is ready for merging, open a pull request
  > - After someone else has reviewed and signed off on the feature, you can merge it into master
  > - Once it is merged and pushed to ‘master’, you can and should deploy immediately


## Sprint Planning

### Histórias, tarefas for história e seus respectivos responsáveis

- [ ] **Cadastrar um produto** 
  - [ ] Criar tela do cadastro do produto - _Guilherme Miranda_
  - [x] Criar um método POST para inserção dos dados no banco - _Tomaz Gomes_
  - [x] Criar estrutura no banco para armazenar os dados do produto - _Lorena Leão_
  - [ ] Criar método para cadastrar imagens no back-end - _Raphael Augusto_

- [ ] **Cadastrar estabelecimento**
  - [ ] Criar tela do cadastro do estabelecimento - _Guilherme Miranda_
  - [x] Criar um método POST para inserção dos dados no banco - _Raphael Augusto_
  - [x] Criar estrutura no banco para armazenar os dados do estabelecimento - _Lorena Leão_

- [ ] **Fazer pesquisa na base de dados**
  - [ ] Criar tela para pesquisa de produto - _Matheus Guilherme Veloso_
  - [x] Criar método GET para fazer pesquisa no banco de produto - _Tomaz Gomes_
  - [x] Criar método GET para fazer pesquisa de lojas - _Tomaz Gomes_
  - [ ] Criar método GET para fazer pesquisa por categorias - _Tomaz Gomes_
  - [ ] Criar métodos para ordenação na interface - _Matheus Guilherme Veloso_
  - [ ] Criar métodos para filtros na interface - _Matheus Guilherme Veloso_

  No backlog (tarefas a serem implementadas se sobrar tempo)
  - [ ] Filtrar pesquisa por Geolocalização

- [ ] **Cadastrar-se no sistema**
  - [ ] Criar tela de cadastro - _Guilherme Miranda_
  - [ ] Criar tela de exbir o perfil do usuário (essa tela pode ser editada e possui botão de exclusão) - _Matheus Guilherme Veloso_
  - [x] Criar tabela dos usuários - _Lorena Leão_
  - [x] Criar métodos CRUD para o usuário - _Raphael Augusto_

- [ ] **Avaliar produto**
  - [x] Criar tabela no banco que guarda as avaliações do produto - _Lorena Leão_
  - [ ] Criar tela de exibição do produto com campo de avaliação - _Matheus Guilherme Veloso_
  - [ ] Criar métodos CRUD - _Tomaz Gomes_

- [ ] **Atualizar dados do produto**
  - [x] Criar estrutura para requisição de atualização no banco - _Lorena Leão_
  - [ ] Criar uma tela para inserir a requisição de atualização do produto - _Guilherme Miranda_
  - [ ] Criar método que verifica se uma quantidade X de requisições foi feita, e após este número de requisições, o valor mais frequente se torna o valor oficial do produto. - _Raphael Augusto_

- [ ] **Avaliar Estabelecimentos**
  - [ ] Criar tela que exibe informações do estabelecimento com os campos de avaliação - _Guilherme Miranda_
  - [ ] Criar métodos CRUD - _Tomaz Gomes_
  - [ ] Criar estruturas no banco para armazenar as avaliações - _Lorena Leão_

- [ ] **Observar o histórico das atualizações do produto**
  - [ ] Criar na tela de exibição do produto a interface de exibição do histórico de atualizações do produto - _Matheus Guilherme Veloso_
  - [ ] Criar métodos CRUD - _Tomaz Gomes_
  - [x] Criar estrutura no banco pra armazenar o histórico de atualização - _Lorena Leão_

- [ ] **Comparar produtos**
  - [ ] Criar uma tela para exibir os produtos comparados - _Guilherme Miranda_
