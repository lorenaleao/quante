# quante
Quanté? é um aplicativo mobile que permite aos usuários pesquisar preços de produtos e serviços. 

Será desenvolvido como um trabalho para a disciplina de [Engenharia de Software](https://github.com/aserg-ufmg/CursoEngenhariaSoftware) (2020/1).

## Sprint Planning

**TODO**: Atribuir tarefas aos integrantes do grupo

- [ ] Cadastrar um produto 
  - [ ] Criar tela do cadastro do produto
  - [ ] Criar um método POST para inserção dos dados no banco
  - [ ] Criar estrutura no banco para armazenar os dados do produto

- [ ] Cadastrar estabelecimento
  - [ ] Criar tela do cadastro do estabelecimento
  - [ ] Criar um método POST para inserção dos dados no banco
  - [ ] Criar estrutura no banco para armazenar os dados do produto

- [ ] Fazer pesquisa na base de dados
  - [ ] Criar tela para pesquisa de produto
  - [ ] Criar método GET para fazer pesquisa no banco de produto
  - [ ] Criar método GET para fazer pesquisa de lojas
  - [ ] Criar método GET para fazer pesquisa por categorias
  - [ ] Criar métodos para ordenação na interface
  - [ ] Criar métodos para filtros na interface

  - No backlog (tarefas a serem implementadas se sobrar tempo)
  - [ ] Filtrar pesquisa por Geolocalização

- [ ] Cadastrar-se no sistema
  - [ ] Criar tela de cadastro
  - [ ] Criar tela de exbir o perfil do usuário (essa tela pode ser editada e possui botão de exclusão)
  - [ ] Criar tabela dos usuários
  - [ ] Criar métodos CRUD para o usuário

- [ ] Avaliar produto
  - [ ] Criar tabela no banco que guarda as avaliações do produto
  - [ ] Criar tela de exibição do produto com campo de avaliação
  - [ ] Criar métodos CRUD

- [ ] Atualizar dados do produto
  - [ ] Criar estrutura para requisição de atualização no banco
  - [ ] Criar uma tela para inserir a requisição de atualização do produto
  - [ ] Criar método que verifica se uma quantidade X de requisições foi feita, e após este número de requisições, o valor mais frequente se torna o valor oficial do produto.

- [ ] Avaliar Estabelecimentos
  - [ ] Criar tela que exibe informações do estabelecimento com os campos de avaliação
  - [ ] Criar métodos CRUD
  - [ ] Criar estruturas no banco para armazenar as avaliações

- [ ] Observar o histórico das atualizações do produto
  - [ ] Criar na tela de exibição do produto a interface de exibição do histórico de atualizações do produto
  - [ ] Criar métodos CRUD
  - [ ] Criar estrutura no banco pra armazenar o histórico de atualização

- [ ] Comparar produtos
  - [ ] Criar uma tela para exibir os produtos comparados
