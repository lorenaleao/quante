# quante
Quanté? é um aplicativo mobile que permite aos usuários pesquisar preços de produtos e serviços. 

Será desenvolvido como um trabalho para a disciplina de [Engenharia de Software](https://github.com/aserg-ufmg/CursoEngenhariaSoftware) (2020/1).

## Sprint Planning

**TODO**: Atribuir tarefas aos integrantes do grupo

- [ ] Cadastrar um produto 
  - [ ] Criar tela do cadastro do produto @guilhermealbm
  - [ ] Criar um método POST para inserção dos dados no banco @tomaz1502
  - [ ] Criar estrutura no banco para armazenar os dados do produto @lorenaleao
  - [ ] Criar método para cadastrar imagens no back-end @Maharal

- [ ] Cadastrar estabelecimento
  - [ ] Criar tela do cadastro do estabelecimento @guilhermealbm
  - [ ] Criar um método POST para inserção dos dados no banco @Maharal
  - [ ] Criar estrutura no banco para armazenar os dados do produto @lorenaleao

- [ ] Fazer pesquisa na base de dados
  - [ ] Criar tela para pesquisa de produto @MaMiotto
  - [ ] Criar método GET para fazer pesquisa no banco de produto @tomaz1502
  - [ ] Criar método GET para fazer pesquisa de lojas @tomaz1502
  - [ ] Criar método GET para fazer pesquisa por categorias @tomaz1502
  - [ ] Criar métodos para ordenação na interface @MaMiotto
  - [ ] Criar métodos para filtros na interface @MaMiotto

  No backlog (tarefas a serem implementadas se sobrar tempo)
  - [ ] Filtrar pesquisa por Geolocalização

- [ ] Cadastrar-se no sistema
  - [ ] Criar tela de cadastro @guilhermealbm
  - [ ] Criar tela de exbir o perfil do usuário (essa tela pode ser editada e possui botão de exclusão) @MaMiotto
  - [ ] Criar tabela dos usuários @lorenaleao
  - [ ] Criar métodos CRUD para o usuário @Maharal

- [ ] Avaliar produto
  - [ ] Criar tabela no banco que guarda as avaliações do produto @lorenaleao
  - [ ] Criar tela de exibição do produto com campo de avaliação @MaMiotto
  - [ ] Criar métodos CRUD @tomaz1502

- [ ] Atualizar dados do produto
  - [ ] Criar estrutura para requisição de atualização no banco @lorenaleao
  - [ ] Criar uma tela para inserir a requisição de atualização do produto @guilhermealbm
  - [ ] Criar método que verifica se uma quantidade X de requisições foi feita, e após este número de requisições, o valor mais frequente se torna o valor oficial do produto. @Maharal

- [ ] Avaliar Estabelecimentos
  - [ ] Criar tela que exibe informações do estabelecimento com os campos de avaliação @guilhermealbm
  - [ ] Criar métodos CRUD @tomaz1502
  - [ ] Criar estruturas no banco para armazenar as avaliações @lorenaleao

- [ ] Observar o histórico das atualizações do produto
  - [ ] Criar na tela de exibição do produto a interface de exibição do histórico de atualizações do produto @MaMiotto
  - [ ] Criar métodos CRUD @tomaz1502
  - [ ] Criar estrutura no banco pra armazenar o histórico de atualização @lorenaleao

- [ ] Comparar produtos
  - [ ] Criar uma tela para exibir os produtos comparados @guilhermealbm
