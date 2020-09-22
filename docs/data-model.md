# Modelo dos Dados

## Database

Teremos apenas um banco de dados, i.e., uma _database_, para armazenar as informações das quais a nossa aplicação precisará, o **db-quante**.

## Collections

As coleções (ou _collections_) são equivalentes às tabelas em bancos de dados relacionais como o MySQL. Para o _Quanté?_ criaremos 4 dessas estruturas, que serão denominadas: _clients_, _companies_, _products_ e _reviews_. Abaixo está uma descrição dos campos (_fields_) que cada tipo de documento (_document_) conterá. 

### Products


Campo | Tipo | Descrição
:--- | :---: | :---- |
**_id** | ObjectId | objeto de identificação do documento gerado no momento de sua inserção na coleção |
**name** | string | nome do produto ou serviço |
**image** | string | endereço da imagem onde ela está armazenada |
**description** | string | breve descrição do produto |
**spec** | dict from string to string | a ficha técnica do produto, que pode ser utilizada para comparar produtos posteriormente|
**categories** | list | lista de categorias às quais o produto pertence |
**prices** | dict from string to pairs of a float and a list of floats |  `{company: (current_price, [possible_curr_price1, possible_curr_price2...]}` dicionário que armazena o preço do produto em cada estabelecimento que o vende, para cada entrada nessa estrutura também são armazenadas as 5 últimas requisições de mudanças de preço enviadas pelos usuários |
**price_history** | list of pairs | `(date, smallest_price)` lista dos menores preços do produto no último ano |
**reviews** | list of Reviews | as 10 avaliações mais curtidas até o momento pelos usuários |


### Reviews

Campo | Tipo | Descrição
:--- | :---: | :---- |
**_id** | ObjectId | objeto de identificação do documento gerado no momento de sua inserção na coleção |
**product_id** | ObjectId | objeto de identificação do produto ou serviço |
**review_author** | string | nome do cliente autor da avaliação do produto |
**review_rating** | float | nota dada pelo cliente |
**review_text** | string | comentário feito pelo cliente |
**published_date** | date | data em que a avaliação foi publicada |
**is_recommended** | bool | indicador de que o produto é recomendado pelo cliente ou não |
**likes** | int | número de curtidas que essa avaliação recebeu até o momento |

### Companies

Campo | Tipo | Descrição
:--- | :---: | :---- |
**_id** | ObjectId | objeto de identificação do documento gerado no momento de sua inserção na coleção |
**name** | string | nome do estabelecimento |
**cnpj** | string | CNPJ do estabelecimento |
**address** | string | endereço do estabelecimento
**email** | list | e-mail de contato do estabelecimento |
**password** | string | senha que dá ao estabelecimento acesso ao seu perfil no aplicativo |
**create_date** | date | data na qual o perfil do estabelecimento foi criado no aplicativo |

### Clients

Campo | Tipo | Descrição
:--- | :---: | :---- |
**_id** | ObjectId | objeto de identificação do documento gerado no momento de sua inserção na coleção |
**name** | string | nome do cliente |
**age** | string | idade do cliente |
**cpf** | string | CPF do cliente |
**email** | list | e-mail de contato do cliente |
**password** | string | senha que dá ao cliente acesso ao seu perfil no aplicativo |
**create_date** | date | data na qual o perfil do cliente foi criado no aplicativo |


