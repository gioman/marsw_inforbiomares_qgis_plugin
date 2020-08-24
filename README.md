# Plugin para QGIS 3.x para criação e edição de metadados segundo o perfil SNIMar


**FICHA TÉCNICA VERSÃO PARA QGIS 3.x**

TÍTULO: Manual de Utilizador do Plugin para QGIS 3.x para criação e edição de metadados segundo o perfil SNIMar

AUTORIA: Projecto MARSW e INFORBIOMARES

EMAIL: jgoncal@ualg.pt

DATA: Julho 2020

VERSÃO: 3.x


**CONTACTOS VERSÃO PARA QGIS 3.x**

Projecto MARSW

Telefone: +351 289 800 051

E-mail: jgoncal@ualg.pt

Projecto INFORBIOMARES

Telefone: +351 289 800 051

E-mail: ccmar@ualg.pt


**FICHA TÉCNICA ORIGINAL**

TÍTULO: Manual de Utilizador/Instalação do Editor de Metadados SNIMar

AUTORIA: Grupo de Trabalho WP4 SNIMar

EMAIL: suporte.snimar@ipma.pt

DATA: dezembro de 2015

LOCAL: Lisboa

VERSÃO: 2.0.0


**CONTACTOS ORIGINAIS**

IPMA - INSTITUTO PORTUGUÊS DO MAR E DA ATMOSFERA

Rua C do Aeroporto | 1749-077 Lisboa - Portugal

Telefone: +351 218 477 000 | Fax: +351 218 402 468 | E-mail:info@ipma.pt


EMEPC - Estrutura de Missão para a Extensão da Plataforma Continental

Rua Costa Pinto nº165 | 2770-047 Paço de Arcos - Portugal

Telefone: +351 213 004 165 | Fax: +351 213 905 225 | E-mail: info@emepc.mam.gov.pt



Introdução
==========

O “**Plugin para criação e edição de metadados segundo o perfil SNIMar**”
é o "*porting*" para a versão 3.x do *software* SIG QGIS (https://www.qgis.org) do editor de Metadados desenvolvido no âmbito do Projecto SNIMar com o objectivo de ser a ferramenta destinada à criação dos metadados em conformidade com o Perfil de Metadados SNIMar. **O trabalho de migração do código para QGIS 3.x foi realizado no âmbito dos projectos MARSW e INFORBIOMARES**.

**Editor de Metadados SNIMar**
foi desenvolvido no âmbito do Projeto SNIMar (http://editor.snimar.pt/)  com o objetivo de ser a ferramenta destinada à criação de metadados em conformidade com o Perfil de Metadados SNIMar. O Editor consiste num *plugin* para a aplicação QGIS, permitindo que a criação de metadados seja feita em paralelo e em simultâneo com a criação e edição de Conjuntos de Dados Geográficos (CDG).

O SNIMar é um projeto nacional, financiado pelo Mecanismo Financeiro do Espaço Económico Europeu 2009-2014 no âmbito dos European Economic Area Grants (EEA Grants), que tem por objetivo o desenvolvimento de uma infraestrutura de dados espaciais marinhos para o aumento da capacidade de avaliação e previsão do estado ambiental das águas marinhas. Esta infraestrutura traduz-se num Geoportal que irá potenciar a interação do público com a informação disponibilizada pelos parceiros e entidades participantes do projeto e constituirá um ponto central de agregação, pesquisa e distribuição de informação geográfica sobre o ambiente marinho em Portugal.

Os metadados de informação geográfica não são mais do que uma descrição textual, de forma normalizada, da informação geográfica. A sua documentação é indispensável para a identificação e avaliação técnica (escala, sistema de referência, qualidade, extensão geográfica e temporal, contactos dos responsáveis) dos CDG, assim como aspetos ligados ao acesso e utilização de serviços de informação geográfica. Pesquisas feitas em sistemas de informação, infraestruturas de dados espaciais (IDE) ou sistemas de comércio eletrónico, são suportadas pelos metadados, que funcionam como o “combustível” para encontrar os recursos desejados.

O Perfil de Metadados SNIMar, definido no âmbito do referido projeto, respeita os requisitos da
Diretiva INSPIRE (Diretiva n.º 2007/2/CE, do Parlamento Europeu e do Conselho, de 14 de março) e as respetivas disposições de execução definidas no Regulamento (CE) n.º 1205/2008 da Comissão, de 3 de dezembro, que estabelece os requisitos aplicáveis à criação e manutenção de metadados para conjuntos de dados geográficos (CDG), séries de conjuntos de dados geográficos e serviços de dados geográficos correspondentes aos temas enumerados nos anexos I, II e III da Diretiva 2007/2/CE. É também importante realçar que o Perfil de Metadados SNIMar teve por base o Perfil Nacional de Metadados de Informação Geográfica (Perfil MIG), que “tem como objetivo principal clarificar aspetos ligados à implementação da produção, gestão e disseminação dos metadados em Portugal, de forma a assegurar a correta caracterização dos recursos geográficos e a sua harmonização com a infraestrutura de informação geográfica portuguesa (SNIG) e europeia (INSPIRE).” [Perfil MIG, 2010], ajustando-se este perfil à realidade nacional dos dados relativos ao ambiente marinho.


Instalação
==========

O *plugin* **EditorMetadadosMarswInforbiomares** foi desenvolvido para operar nos sistemas operativos Linux, Windows e macOS e pode ser instalado na aplicação QGIS da seguinte forma:

*   Abrir a aplicação QGIS, recomenda-se a utilização da versão 3.10

*   No Menu Principal selecionar **Módulos > Gerir e Instalar Módulos**

*   Selecionar o separador **Configurações**

*   Adicionar um novo repositório de módulos, premindo o botão “Adicionar...”, e preencher os campos do formulário com os seguintes parâmetros:

    *   *Nome*: Editor Metadados MarSW/Inforbiomares
    
    *   *URL*: https://marsw.ualg.pt/static/qgis/editormetadadosmarswinforbiomares.xml

    *   *Parâmetros*: manter pré-definições
    
    *   *Ativado*: manter pré-definições

*   Fazer “Ok” e atualizar os repositórios premindo o botão “Atualizar todos os repositórios”.

*   Selecionar o separador **Não instalado** e pesquisar por “MarSW” ou “Inforbiomares” ou “SNIMar”

*   Instalar p *plugin* através do botão “Instalar módulo”

O *plugin* **EditorMetadadosMarswInforbiomares** ficará ativo e disponível no menu de ferramentas através do ícone <img src="http://193.136.227.146/manual_images/100000000000004000000040A7A1CB042E5963C1.png" width="25">


Plugin para QGIS 3.x para criação e edição de metadados segundo o perfil SNIMar
===============================================================================

Ao premir o ícone do **EditorMetadadosMarswInforbiomares** terá acesso a uma janela que, para além de um Menu Principal, terá um Separador com o seu ambiente de trabalho (Lista de Ficheiros), ou seja, uma Lista dos documentos de metadados (ficheiros XML) trabalhados a partir deste Editor. Atenção que enquanto não criar novos metadados ou abrir outros já existentes, a partir do editor, esta Lista aparecerá vazia no seu ambiente de trabalho.


**Nota**: Ao fazer duplo *click* em ficheiros da Lista estes são abertos como novos Separadores em modo de edição.

Ambiente de Trabalho
--------------------

Nesta área poderá gerir os seus documentos de metadados e consultar alguma da sua informação base (Tipo de Recurso, Título, Localização (do ficheiro), Identificador Único do Ficheiro, Conformidade com o Perfil SNIMar.

O botão <img src="http://193.136.227.146/manual_images/100002010000002100000021EFB2E74358139587.png"> permite validar automaticamente o documento quanto à sua conformidade com o Perfil SNIMar.

Ao selecionar um documento de metadados da Lista e abrindo o *Menu de Contexto* (*click* com o botão do lado direito do rato) tem acesso às seguintes funcionalidades:

*   **Editar Metadado**: abrir o documento XML no *plugin* em modo de edição;

*   **Remover Metadado(s) da Lista**: remover o(s) documento(s) XML selecionado(s) da Lista;

*   **Visualizar Metadado Externamente**: abrir o documento XML no *software* pré-definido para ficheiros XML.


Na parte inferior da janela (lado direito) tem dois botões com as seguintes funcionalidades:

*   **Verificar Conformidade (Todos)**: validar todos os documentos da Lista quanto à sua conformidade com o Perfil SNIMar. Esta ação pode demorar consoante o número de itens na Lista, pode a qualquer momento terminar o processo premindo o botão “Cancelar” da janela de progresso.

*   **Apagar Lista de Ficheiros**: remover todos os documentos XML da Lista (apenas).

Na parte inferior da janela (lado esquerdo) poderá ainda consultar qual a última *versão do Thesaurus SNIMar* carregada no *plugin* e poderá descarregar novas atualizações, se existirem, premindo o botão “Atualizar”.

É possível também *ordenar a Lista de ficheiros de metadados* por: Tipo de Recurso, Título, Localização (do ficheiro) e pela sua Conformidade com o Perfil SNIMar; basta premir o título correspondente e alternar a ordem.

A partir do **Menu Principal** poderá:

*   **Ficheiro > Novo**: criar um novo documento de metadados XML dos seguintes tipos: Conjunto de Dados Geográficos, Serviço e Série.

*   **Ficheiro > Abrir**: abrir um documento XML, a partir do sistema de arquivo de ficheiros, no *plugin* em modo de edição. Este documento de metadados aberto será também adicionado à Lista de ficheiros.

*   **Ficheiro > Abrir Pasta**: carregar para o seu ambiente de trabalho os ficheiros XML que se encontrarem na pasta selecionada a partir do sistema de arquivo de ficheiros.

*   **Ficheiro > Guardar**: guardar as alterações efetuadas ao documento XML a partir do *plugin* de edição.

*   **Ficheiro > Guardar como**: guardar o ficheiro com outro nome ou noutro diretório.

*   **Ficheiro > Guardar Todos**: guardar todos os ficheiros de metadados abertos no editor.

*   **Ficheiro > Fechar**: fechar o *plugin* **EditorMetadadosMarswInforbiomares**.

*   **Ficheiro > Atualizar codelists**:atualiza os campos do tipo Lista de Valores dos vários formulários.

*   **Lista de Contactos**: gerir (adicionar / editar / remover) os contactos e respetivos detalhes usados frequentemente nos seus documentos de metadados.

*   **Sobre** : abrir uma janela com informações sobre o *plugin* **EditorMetadadosMarswInforbiomares**.


Gestão de Contactos
-------------------

Ao selecionar a opção “Lista de Contactos” do Menu Principal abrirá uma janela que apresenta na parte lateral esquerda uma Lista de contactos já criados e na parte lateral direita o formulário de edição dos contactos.

Ao criar um novo contacto deverá preencher obrigatoriamente os campos “Nome da Organização” e “Endereço Eletrónico” (pelo menos um), os
restantes campos são opcionais mas aconselha-se o seu preenchimento.

**Criar um Novo Contacto**

*   prima o botão “Novo”;

*   preencha os campos;

*   prima o botão “Guardar Alterações”.


**Editar um Contacto**

*   selecione da Lista o contacto em questão;

*   efetue as alterações a partir do formulário agora preenchido com os detalhes do contacto selecionado;

*   prima o botão “Guardar Alterações”.


**Apagar um Contacto**

*   selecione da Lista o contacto em questão;

*   prima o botão “Apagar”.

*   Receberá uma mensagem a pedir confirmação da eliminação do contacto dado que é uma operação irreversível. Para confirmar a eliminação prima o botão “Remover”.


**Notas:** Alguns campos permitem a introdução de *múltiplos valores*, como é o caso do “Telefone”, “Fax”, “Endereço Eletrónico” e “Informação Online”. Para preencher estes campos deverá preencher o campo de texto posicionado em baixo da Lista respetiva a cada um deles (com textos exemplo) e premir o botão
<img src="http://193.136.227.146/manual_images/100002010000019300000193BC9FD78E936508CD.png" width="25">.

Para remover da Lista terá de selecionar a opção que pretende eliminar e primir o botão <img src="http://193.136.227.146/manual_images/10000201000001930000019328914E2E388B62C5.png" width="25">.

Edição de Metadados
-------------------

Ao criar ou abrir um documento de metadados será criada, na janela do *plugin*, um novo Separador com o formulário de preenchimento de metadados. Ao abrir um documento de metadados os campos, reconhecidos pelo editor, serão preenchidos nos campos respetivos de forma automática. Os campos variam consoante o tipo de recurso em questão.

O formulário de preenchimento de metadados está dividido em secções, listadas na parte lateral esquerda do Separador, que agrupam de forma lógica os campos de metadados. Na parte lateral direita é apresentado o Painel com os campos que pertencem à secção selecionada na parte esquerda.

A lista de secções é a seguinte:

*   Identificação;

*   Operações (exclusivo a recursos do tipo “Serviço”);

*   Classificação & Palavras-Chave;

*   Informação Geográfica;

*   Informação Temporal;

*   Qualidade;

*   Restrições;

*   Distribuição;

*   Metadados.


Na parte lateral esquerda, onde são listadas as secções, terá indicações de validação da conformidade do preenchimento do metadado. As secções a vermelho estarão não conformes e as a preto conformes. Ao passar com o rato sobre cada secção a vermelho terá a indicação específica dos campos que não estão conformes.

De igual forma os painéis na parte lateral direita também apresentam ajudas textuais para cada um dos campos (premir o botão de informação junto ao nome de cada campo) e indicações de validação. Os campos com “*” são de preenchimento obrigatório e enquanto não forem preenchidos corretamente encontram-se a vermelho.

Alguns campos permitem a introdução de *múltiplos valores*, para os adicionar deverá preencher o campo (com textos exemplo) ou selecionar de um campo de lista de valores posicionados em baixo da Lista / Tabela respetiva e premir o botão <img src="http://193.136.227.146/manual_images/100002010000019300000193BC9FD78E936508CD.png" width="25">. Para remover uma opção da Lista selecione a opção a eliminar e prima o botão <img src="http://193.136.227.146/manual_images/10000201000001930000019328914E2E388B62C5.png" width="25">.

Pode remover mais do que um de uma vez, para tal só terá de fazer uma multi‑seleção de opções (CTRL+*click*) antes de premir o botão de eliminar. Alguns campos do tipo Lista de Valores têm para cada opção da lista uma ajuda textual, para as visualizar basta posicionar o rato sobre as opção da lista.

Cada painel contém um conjunto de elementos e sub‑elementos a preencher. De seguida, descrevem-se cada um destes painéis, respetivos campos e sua obrigatoriedade (*) e multiplicidade de preenchimento.

**Identificação**

Informação de base necessária à identificação inequívoca de um dado recurso. Contém os seguintes elementos e sub‑elementos:

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Tipo de Recurso | Sim     | Não      | Define o tipo de recurso ao qual se aplicam os metadados, a partir de uma lista: Conjunto de Dados Geográficos (CDG) (a informação é aplicável a um conjunto de dados geográficos); Série (a informação é aplicável a uma série ou coleção de dados); Serviço (a informação é aplicável à capacidade que uma entidade fornecedora disponibiliza a uma entidade cliente através de um conjunto de interfaces que define um dado comportamento). |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Tipo de Serviço | Sim     | Não      | Define o tipo de serviço, a partir da lista definida pela especificação do INSPIRE. Não se aplica a CDG nem Séries. |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Acoplamento     | Sim     | Não      | Tipo de acoplamento dos serviços com os CDG. Não se aplica a CDG nem Séries. |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Título          | Sim     | Não      | Designação pela qual o recurso é conhecido. O título deve permitir identificar o recurso com o maior rigor possível. Recomenda-se a tradução deste campo para Inglês no campo Título (Inglês). |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Resumo          | Sim     | Não      | Breve resumo sobre o conteúdo do recurso. Recomenda-se a tradução deste campo para Inglês no campo Resumo (Inglês). |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Resumo          | Sim     | Não      | Breve resumo sobre o conteúdo do recurso. Recomenda-se a tradução deste campo para Inglês no campo Resumo (Inglês). |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Resumo          | Sim     | Não      | Breve resumo sobre o conteúdo do recurso. Recomenda-se a tradução deste campo para Inglês no campo Resumo (Inglês). |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Resumo          | Sim     | Não      | Breve resumo sobre o conteúdo do recurso. Recomenda-se a tradução deste campo para Inglês no campo Resumo (Inglês). |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Título Alternativo          | Não     | Não      | Nome alternativo ou abreviado pelo qual o recurso é conhecido. |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |                                                                             |
| Objetivo          | Não     | Não      | Resumo do propósito que conduziu ao desenvolvimento ou modificação do recurso. |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Créditos | Não      | Sim      | Identificação dos indivíduos e/ou entidades que contribuíram para a produção do recurso. |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Manutenção do Recurso | Sim      | Sim      | Define a frequência com que o recurso é atualizado, a partir de uma lista. Se nenhuma das opções da lista for adequada, selecione "Conforme necessário". |

| Elemento        | Obrig.* | Múltiplo | Definição |
| ---             | ---     | ---      | ---       |
| Identificador Único do Recurso | Sim      | Sim      | Pretende identificar de forma unívoca o recurso, é definido normalmente pela entidade responsável pelo mesmo. Pode conter múltiplos conjuntos dos seguintes sub‑elementos. |
| Identificador                  | Sim      | Não      | Utilização de URI (exº http://www.igeo.pt/datasets/AU_CAOP_2011) ou UUID (exº 808c3be3-527a-451b-8611-0bcc1b8c21b0).                                                       |
| Espaço de Nomes                | Não      | Não      | Define o âmbito de aplicação do código usado acima.                                                                                                                        


+-----------------------------------------------------------------------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento                                                                                                                    | Obrig. *     | Múltiplo | Definição                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                             |              |          |                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Resolução Espacial                                                                                                          | Sim          | Sim      | Nível de detalhe do recurso, expresso como um fator de escala ou como uma distância no terreno.                                                                                                                                                                                                                                                                                    |
| ^^^^^^^^^^^^^^^^^^                                                                                                          |              |          | Pode conter múltiplos valores dos seus sub‑elementos. Caso se desconheça este elemento e, sendo que é obrigatório, selecione a                                                                                                                                                                                                                                                     |
|                                                                                                                             |              |          | *checkbox *                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                             |              |          | “Resolução Espacial Desconhecida”.                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                             |              |          |                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Escala Equivalente                                                                                                          | Condi-cional | Sim      | Para um recurso em formato analógico ou conjuntos digitais para impressão é a escala de representação. No caso de recursos digitais a escala deverá corresponder a um compromisso entre a resolução espacial (da informação matricial de origem) e/ou erro do levantamento (precisão dos equipamentos de aquisição utilizados) e o erro de graficismo convertido à escala da carta |
|                                                                                                                             |              |          | que se pretende                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                             |              |          | imprimir.                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                             |              |          |                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Distância                                                                                                                   | Condi-cional | Sim      | Nível de detalhe dos dados expresso em GSD (                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                             |              |          | *Ground Sample Distance*                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                             |              |          | ). Para conjuntos de dados vetoriais que não têm uma escala associada ou não são produzidos para serem disponibilizados em formato analógico, pode-se usar este elemento para descrever a precisão estimada na aquisição dos dados. Expressa em metros.                                                                                                                            |
|                                                                                                                             |              |          |                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Este elemento é obrigatório apenas para CDG e Séries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Para dados vetoriais utiliza-se normalmente a escala (denominador), para dados matriciais a distância no terreno em metros.                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


+-------------+----------+----------+-------------------------------------------------------------+
| Elemento    | Obrig. * | Múltiplo | Definição                                                   |
|             |          |          |                                                             |
+-------------+----------+----------+-------------------------------------------------------------+
| Codificação | Não      | Não      | Define a codificação informática de caracteres utilizada no |
| ^^^^^^^^^^^ |          |          | recurso                                                     |
|             |          |          | , a partir de uma lista                                     |
|             |          |          | . Não se aplica a Serviços.                                 |
|             |          |          |                                                             |
+-------------+----------+----------+-------------------------------------------------------------+


+-------------------+----------+----------+-----------------------------------------------------------------+
| Elemento          | Obrig. * | Múltiplo | Definição                                                       |
|                   |          |          |                                                                 |
+-------------------+----------+----------+-----------------------------------------------------------------+
| Estado do Recurso | Não      | Sim      | Define o estado de progresso do recurso, a partir de uma lista: |
| ^^^^^^^^^^^^^^^^^ |          |          | *Arquivado*                                                     |
|                   |          |          | (dados foram armazenados numa infraestrutura de armazenamento   |
|                   |          |          | *offline*                                                       |
|                   |          |          | );                                                              |
|                   |          |          | *Concluído*                                                     |
|                   |          |          | (produção dos dados foi concluída);                             |
|                   |          |          | *Contínuo*                                                      |
|                   |          |          | (dados são atualizados continuamente);                          |
|                   |          |          | *Em desenvolvimento*                                            |
|                   |          |          | (dados estão atualmente em processo de criação);                |
|                   |          |          | *Necessita de atualização*                                      |
|                   |          |          | (dados necessitam de atualização);                              |
|                   |          |          | *Obsoleto*                                                      |
|                   |          |          | (dados já não são relevantes);                                  |
|                   |          |          | *Planeado*                                                      |
|                   |          |          | (estabelecida uma data fixa na qual os dados são atualizados).  |
|                   |          |          |                                                                 |
+-------------------+----------+----------+-----------------------------------------------------------------+


+---------------------+----------+----------+--------------------------------------------------------+
| Elemento            | Obrig. * | Múltiplo | Definição                                              |
|                     |          |          |                                                        |
+---------------------+----------+----------+--------------------------------------------------------+
| Recursos Associados | Não      | Sim      | O domínio deste elemento é um URI, que pode ser um     |
| ^^^^^^^^^^^^^^^^^^^ |          |          |                                                        |
|                     |          |          | identificador do CDG, ou uma localização (URL) para os |
|                     |          |          |                                                        |
|                     |          |          | metadados do(s) CDG associados ao recurso.             |
|                     |          |          |                                                        |
|                     |          |          | Não se aplica a CDG nem Séries.                        |
|                     |          |          |                                                        |
+---------------------+----------+----------+--------------------------------------------------------+


+----------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Elemento                               | Obrig. * | Múltiplo | Definição                                                                                              |
|                                        |          |          |                                                                                                        |
+----------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Endereço (URL da visualização gráfica) | Não      | Não      | Define o caminho (URL) para uma figura que ilustra o recurso (deve incluir uma legenda para a figura). |
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                        |
|                                        |          |          |                                                                                                        |
+----------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+


+----------+----------+----------+------------------------------------+
| Elemento | Obrig. * | Múltiplo | Definição                          |
|          |          |          |                                    |
+----------+----------+----------+------------------------------------+
| Idioma   | Não      | Sim      | Idioma(s) utilizado(s) no recurso. |
| ^^^^^^   |          |          |                                    |
|          |          |          | Não se aplica a Serviços.          |
|          |          |          |                                    |
+----------+----------+----------+------------------------------------+


+------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento               | Obrig. * | Múltiplo | Definição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Representação Espacial | Sim      | Sim      | Forma(s) de representação da informação geográfica, a partir de uma lista: Matricial (informação geográfica segue um modelo de dados matricial); Modelo Estereoscópico (vista tridimensional formada pela intersecção de raios homólogos resultantes de um par de imagens com sobreposição); TIN (informação geográfica representa-se de acordo com uma tecelagem irregular triangular TIN); Texto Tabela (informação geográfica encontra-se codificada em formato textual ou tabular); Vectorial (informação geográfica segue um modelo de dados vetorial); Video (cena obtida de uma gravação de vídeo). |
| ^^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                        |          |          | Não se aplica a Serviços.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento                                                               | Obrig. * | Múltiplo | Definição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Responsáveis pelo Recurso                                              | Sim      | Sim      | Informações necessárias para permitir o contacto com a pessoa e / ou organização responsável pelo recurso.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ^^^^^^^^^^^^^^^^^^^^^^^^^                                              |          |          | Pode conter múltiplos conjuntos dos seguintes sub‑elementos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Função                                                                 | Não      | Não      | Função desempenhada pela organização responsável, a partir de uma lista: Autor (entidade responsável pela autoria dos recursos); Contacto (entidade / pessoa contactável para obtenção dos recursos ou de informação sobre os recursos); Contacto do Processo (entidade / pessoa que participou em algum processo conducente à modificação dos recursos); Detentor (entidade detentora dos direitos de propriedade sobre os recursos); Editor (entidade que publicou os recursos); Fornecedor (entidade que fornece os recursos); Investigador Principal (entidade de nível hierárquico superior responsável pela recolha da informação e orientação da investigação); Produtor (entidade produtora dos recursos); Tutor (entidade responsável pela tutela dos dados e pela manutenção dos recursos); Utilizador (entidade que utilizada os recursos). |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nome                                                                   | Não      | Não      | Nome da pessoa responsável.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Organização                                                            | Sim      | Não      | Nome da organização responsável.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                        |          |          | Poderá selecionar de uma Lista de valores ou preencher de forma livre no campo “Outra (não listada)”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Morada                                                                 | Não      | Não      | Morada da pessoa ou organização responsável.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cidade                                                                 | Não      | Não      | Cidade da pessoa ou organização responsável.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Código-Postal                                                          | Não      | Não      | Código-Postal da pessoa ou organização responsável.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| País                                                                   | Não      | Não      | País                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                        |          |          | ** **                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                        |          |          | da pessoa ou organização responsável.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Telefone                                                               | Não      | Sim      | Número(s) de telefone da organização ou indivíduo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fax                                                                    | Não      | Sim      | Número(s) de fax da organização ou indivíduo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Endereço Eletrónico                                                    | Sim      | Sim      | Endereço(s) Eletrónico(s) da organização ou indivíduo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Informação                                                             | Não      | Não      | Informação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| *Online*                                                               |          |          | *online *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                        |          |          | (endereço URL / URI)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                        |          |          | que pode ser usada como contacto individual ou institucional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                        |          |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| : Este elemento disponibiliza as seguintes funcionalidades / botões:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| “Adicionar Contacto” Para adicionar um novo contacto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| |10000A990000034F0000034F635B68E6E0D88521_svg|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| |100002010000002000000020A3F87039BE9D0D7E_png|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Para importar um contacto da sua Lista de Contactos para o formulário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| |1000083700002D5300002D534093D958E24AE6E2_svg|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| |10000201000001B7000001B78F0FC5D379C32E50_png|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Para guardar o contacto na sua Lista de Contactos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| |1000136C0000026100000261C06770E50C4736EF_svg|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| |100002010000001700000017FBA90A52D3565DE1_png|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Para remover o contacto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




Operações
~~~~~~~~~

Informação sobre todas as operações disponibilizadas por um Serviço, logo só é preenchido para recursos do tipo “Serviço”. Contém os seguintes elementos e sub‑elementos:


+-----------------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento                          | Obrig. * | Múltiplo | Definição                                                                                                                                                                     |
|                                   |          |          |                                                                                                                                                                               |
+-----------------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Operações                         | Sim      | Sim      | Informação sobre as operações disponibilizadas pelo serviço.                                                                                                                  |
| ^^^^^^^^^                         |          |          |                                                                                                                                                                               |
|                                   |          |          | Para criar uma nova Operação prima o                                                                                                                                          |
|                                   |          |          | botão                                                                                                                                                                         |
|                                   |          |          | “Adicionar Operação”.                                                                                                                                                         |
|                                   |          |          |                                                                                                                                                                               |
|                                   |          |          | Deve ser preenchido com um URL para um documento que descreva a interface do serviço, como por exº o GetCapabilities ou um documento WSDL, mais exemplos apresentados abaixo. |
|                                   |          |          |                                                                                                                                                                               |
+-----------------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nome da Operação                  | Sim      | Não      | Identificador único para um interface específico de um serviço; por exº: "GetCapabilities".                                                                                   |
|                                   |          |          |                                                                                                                                                                               |
+-----------------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DCP (                             | Sim      | Sim      | Define a(s) plataforma(s) computacional(ais) em que a operação foi implementada, a partir de uma lista.                                                                       |
| *Distributed Computing Platforms* |          |          |                                                                                                                                                                               |
| )                                 |          |          | O valor por omissão deve ser “WebServices”.                                                                                                                                   |
|                                   |          |          |                                                                                                                                                                               |
+-----------------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pontos de Acesso (URI/URL)        | Sim      | Sim      | Ponto de acesso. URL que acede ao documento.                                                                                                                                  |
|                                   |          |          |                                                                                                                                                                               |
|                                   |          |          | O preenchimento deste sub‑elemento, não substitui o preenchimento do Localizador do Recurso referido no Painel “Distribuição”.                                                |
|                                   |          |          |                                                                                                                                                                               |
+-----------------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Exemplos de
*Nomes de Operação WMS*
:

*   GetCapabilities;



*   GetMap;



*   GetFeatureInfo;



*   DescribeLayer;



*   GetLegendGraphic.


    Exemplos de
    *Nomes de Operação WFS*
    :



*   GetCapabilities;



*   DescribeFeatureType;



*   GetFeature;



*   LockFeature;



*   Transaction;



*   GetPropertyValue (versão 2.0.0 apenas);



*   GetFeatureWithLock (versão 2.0.0 apenas);



*   CreateStoredQuery (versão 2.0.0 apenas);



*   DropStoredQuery (versão 2.0.0 apenas);



*   ListStoredQueries (versão 2.0.0 apenas);



*   DescribeStoredQueries (versão 2.0.0 apenas);



*   GetGMLObject (versão 1.1.0 apenas).


    Exemplos de
    *Nomes de Operação WCS*
    :



*   GetCapabilities;



*   DescribeCoverage;



*   GetCoverage.



Classificação & Palavras-Chave
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Informação geral que categoriza e descreve um dado recurso. Contém os seguintes elementos e sub‑elementos:


+---------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento      | Obrig. * | Múltiplo | Definição                                                                                                                                                                                                         |
|               |          |          |                                                                                                                                                                                                                   |
+---------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Temas INSPIRE | Sim      | Sim      | Se o recurso for um CDG ou Série, deve ser fornecida, pelo menos, uma palavra-chave do Thesaurus Geral Multilingue sobre Recursos Ambientais (GEMET) que descreva o tema de dados geográficos relevante, conforme |
| ^^^^^^^^^^^^^ |          |          |                                                                                                                                                                                                                   |
|               |          |          | definido nos anexos I, II ou III da Diretiva INSPIRE (Anexo A). Estes elemento é definido a partir de uma lista.                                                                                                  |
|               |          |          |                                                                                                                                                                                                                   |
|               |          |          | Não se aplica a Serviços.                                                                                                                                                                                         |
|               |          |          |                                                                                                                                                                                                                   |
+---------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


+----------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------+
| Elemento                   | Obrig. * | Múltiplo | Definição                                                                                                       |
|                            |          |          |                                                                                                                 |
+----------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------+
| Classificação dos Serviços | Sim      | Sim      | Se o recurso for um Serviço, deve ser fornecida, pelo menos, uma palavra-chave da classificação dos serviços de |
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                                 |
|                            |          |          | dados geográficos, definido a partir de uma lista.                                                              |
|                            |          |          |                                                                                                                 |
|                            |          |          | Poderá consultar uma descrição acerca de cada uma das opções desta lista em Anexo.                              |
|                            |          |          |                                                                                                                 |
|                            |          |          | Não se aplica a CDG nem Séries.                                                                                 |
|                            |          |          |                                                                                                                 |
+----------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------+


+--------------------+----------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento           | Obrig. * | Múltiplo | Definição                                                                                                                                                                       |
|                    |          |          |                                                                                                                                                                                 |
+--------------------+----------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Categoria Temática | Sim      | Sim      | Tema principal do recurso. Define a classificação temática geral utilizada para auxiliar o agrupamento e pesquisa do recurso, a partir de uma lista.                            |
| ^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                                                                                                 |
|                    |          |          | De acordo com o Perfil SNIMar o tema “Oceanos” deverá estar sempre selecionado. Ao criar um documento de metadados via este editor esta condição será automaticamente aplicada. |
|                    |          |          |                                                                                                                                                                                 |
|                    |          |          | Não se aplica a Serviços.                                                                                                                                                       |
|                    |          |          |                                                                                                                                                                                 |
+--------------------+----------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


+-----------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento              | Obrig. * | Múltiplo | Definição                                                                                                                                                                          |
|                       |          |          |                                                                                                                                                                                    |
+-----------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Palavras-Chave Livres | Não      | Sim      | Este elemento permite introduzir outras palavras-chave, livres ou associadas a um léxico, que caracterizam o recurso. Pode conter múltiplos conjuntos dos seguintes sub‑elementos. |
| ^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                                                                                                    |
|                       |          |          |                                                                                                                                                                                    |
+-----------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Palavra-Chave         | Não      | Não      | Texto utilizado para descrever um determinado aspeto do recurso.                                                                                                                   |
|                       |          |          |                                                                                                                                                                                    |
+-----------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tipo                  | Não      | Não      | Utilizado para agrupar as palavras-chave, definido a partir de uma lista.                                                                                                          |
|                       |          |          |                                                                                                                                                                                    |
+-----------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Thesaurus             | Não      | Não      | Nome do léxico, thesaurus ou fonte de palavras-chave formalmente registado.                                                                                                        |
|                       |          |          |                                                                                                                                                                                    |
+-----------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data                  | Não      | Não      | Data de referência do léxico citado.                                                                                                                                               |
|                       |          |          |                                                                                                                                                                                    |
+-----------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tipo de Data          | Não      | Não      | Evento usado para a data referenciada, definido a partir de uma lista.                                                                                                             |
|                       |          |          |                                                                                                                                                                                    |
+-----------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+---------------------------------------------------------------------------------------------------------+
| Elemento                                                                                                                                                                                                                                   | Obrig. * | Múltiplo | Definição                                                                                               |
|                                                                                                                                                                                                                                            |          |          |                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+---------------------------------------------------------------------------------------------------------+
| Palavras-Chave SNIMar                                                                                                                                                                                                                      | Sim      | Sim      | Descreve o recurso utilizando palavras-chave pertencentes a um dicionário dedicado ao projeto SNIMar.   |
| ^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                                                      |          |          | Pode conter múltiplos conjuntos dos seguintes sub‑elementos.                                            |
|                                                                                                                                                                                                                                            |          |          |                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+---------------------------------------------------------------------------------------------------------+
| Tipo                                                                                                                                                                                                                                       | Sim      | Não      | Define o tipo de Palavra-Chave utilizado, a partir de lista.                                            |
|                                                                                                                                                                                                                                            |          |          |                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+---------------------------------------------------------------------------------------------------------+
| Palavra-Chave                                                                                                                                                                                                                              | Sim      | Não      | Define uma designação utilizada para descrever um determinado aspeto do recurso, a partir de uma lista. |
|                                                                                                                                                                                                                                            |          |          |                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+---------------------------------------------------------------------------------------------------------+
| Versão Thesaurus                                                                                                                                                                                                                           | Sim      | Não      | Versão do Thesaurus SNIMar a partir do qual foi selecionada a palavra-chave.                            |
|                                                                                                                                                                                                                                            |          |          |                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+---------------------------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                                                                                                                                                                                                                  |
| : Deve ser escolhida obrigatoriamente pelo menos uma palavra-chave para o tipo “Disciplina” e pelo menos uma palavra-chave para o tipo “Parâmetro”.                                                                                                                                                                                                                        |
| Caso o recurso tenha sido criado no contexto de um projeto, é obrigatório inserir uma palavra-chave com o nome do projeto e usar o tipo de palavra ‘Projeto’.                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                            |
| Recomenda-se a inserção de palavras dos restantes grupos de palavras provenientes do Thesaurus SNIMar, a partir da lista do Thesaurus com a versão mais recente.                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                            |
| Para criar novas palavras-chave SNIMar deverá fazê-lo a partir da plataforma                                                                                                                                                                                                                                                                                               |
| **Collaborative Keywords**                                                                                                                                                                                                                                                                                                                                                 |
| , aceda diretamente premindo o ícone                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                            |
| Para adicionar palavras-chave SNIMar prima o botão “Adicionar Palavra-Chave SNIMar”. Ao executar esta ação é aberta uma janela (figura seguinte) de onde deverá selecionar de início o “Tipo de Palavra-Chave” da lista disponível.                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                            |
| Ao selecionar um Tipo de Palavra-Chave é apresentada na parte lateral direita a lista de palavras-chave relacionadas com esse Tipo. Poderá selecionar múltiplas palavras-chave para acrescentar ao documento acionando os                                                                                                                                                  |
| *checkboxes*                                                                                                                                                                                                                                                                                                                                                               |
| respetivos.                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                            |
| No caso particular do Tipo de Palavra-Chave “Disciplina” após selecionar uma ou mais disciplinas deverá também selecionar um ou mais parâmetros, apresentados na parte lateral mais à direita (à medida que vai selecionando disciplinas).                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                            |
| Após                                                                                                                                                                                                                                                                                                                                                                       |
| acionar as palavras-chave pretendidas deve premir o botão “Adicionar Selecionadas”.                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


|10000000000003A00000027449993894749EB3FE_png|

Informação Geográfica
~~~~~~~~~~~~~~~~~~~~~

Informação sobre os Sistemas de Referência de Coordenadas e sobre a extensão espacial geográfica e altimétrica do recurso. Contém os seguintes elementos e sub‑elementos:


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Elemento                                                                                                                                                                                       | Obrig. * | Múltiplo | Definição                                                                                                             |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Localização Geográfica                                                                                                                                                                         | Sim      | Sim      | Informação sobre a extensão geográfica do recurso. Pode conter múltiplos conjuntos dos seguintes sub‑elementos.       |
| ^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                         |          |          |                                                                                                                       |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Limite Oeste                                                                                                                                                                                   | Sim      | Não      | Coordenada ocidental do limite da extensão do recurso, expressa em longitude utilizando graus decimais.               |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
|                                                                                                                                                                                                |          |          | Coordenada geográfica aproximada a pelo menos 2 casas decimais, posicionado entre o seguinte intervalo: [-180, 180].  |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Limite Este                                                                                                                                                                                    | Sim      | Não      | Coordenada oriental do limite da extensão do recurso, expressa em longitude utilizando graus decimais.                |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
|                                                                                                                                                                                                |          |          | Coordenada geográfica aproximada a pelo menos 2 casas decimais, posicionado entre o seguinte intervalo: [-180, 180].  |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Limite Norte                                                                                                                                                                                   | Sim      | Não      | Coordenada setentrional do limite da extensão do recurso, expressa em latitude utilizando graus decimais.             |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
|                                                                                                                                                                                                |          |          | Coordenada geográfica aproximada a pelo menos 2 casas decimais, posicionado entre o seguinte intervalo: [-90, 90].    |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Limite Sul                                                                                                                                                                                     | Sim      | Não      | Coordenada meridional do limite da extensão do recurso, expressa em latitude utilizando graus decimais.               |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
|                                                                                                                                                                                                |          |          | Coordenada geográfica aproximada a pelo menos 2 casas decimais, posicionado entre o seguinte intervalo: [-90, 90].    |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Contém Recurso                                                                                                                                                                                 | Sim      | Não      | Indica se o retângulo delimitador abrange uma área coberta pelos dados ou uma área onde os dados não estão presentes. |
|                                                                                                                                                                                                |          |          |                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                                                                                                                                                                                    |
| : Para adicionar uma nova extensão geográfica pode fazê-lo de duas formas:                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                              |
| *Manualmente*                                                                                                                                                                                                                                                                                                                                |
| – prima o botão “Adicionar Localização”, é então aberta uma janela onde poderá definir os limites nos campos correspondentes e adicioná-los ao metadados premindo o botão “Adicionar”.                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                              |
| *No Mapa*                                                                                                                                                                                                                                                                                                                                    |
| – prima o botão                                                                                                                                                                                                                                                                                                                              |
| |100016320000327000003270A22C429A68005E8D_svg|                                                                                                                                                                                                                                                                                               |
| |10000201000001E8000001E8CCDB88B34D87F801_png|                                                                                                                                                                                                                                                                                               |
| é então aberta uma janela (figura na página seguinte) onde poderá desenhar um retângulo que represente os limites.                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                              |
| A janela apresenta uma barra de ferramentas de onde pode:                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                              |
| |100016320000327000003270A22C429A68005E8D_svg|                                                                                                                                                                                                                                                                                               |
| |10000201000001E8000001E8CCDB88B34D87F801_png|                                                                                                                                                                                                                                                                                               |
| afastar a visão do mapa à totalidade do globo                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                              |
| |10000544000046A9000046A9C576A73C6EFC279A_svg|                                                                                                                                                                                                                                                                                               |
| |10000201000002AC000002AC93F9F67F6B63BBC7_png|                                                                                                                                                                                                                                                                                               |
| mover o mapa                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| |100005EF0000178100001781273D089BC013EA25_svg|                                                                                                                                                                                                                                                                                               |
| |10000201000000E3000000E3D57FEACA303168F9_png|                                                                                                                                                                                                                                                                                               |
| aproximar a visão do mapa                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                              |
| |1000055D000017810000178195ACBD3347489439_svg|                                                                                                                                                                                                                                                                                               |
| |10000201000000E3000000E3A255E6F26DADD695_png|                                                                                                                                                                                                                                                                                               |
| afastar a visão do mapa                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| |1000050E00002ADA00002ADA3CBB09F56AF59D9E_svg|                                                                                                                                                                                                                                                                                               |
| |100002010000019F0000019F2E58215D7D78FD03_png|                                                                                                                                                                                                                                                                                               |
| desenhar o retângulo - ao desenhar as coordenadas dos limites os campos respetivos na parte inferior da janela são atualizados. Para adicionar o limite ao metadado prima o botão “Adicionar”.                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                              |
| |100002010000001C0000001A19ADBB8A5C169711_png|                                                                                                                                                                                                                                                                                               |
| obter de camada – permite carregar para os campos do formulário a extensão geográfica de um conjunto de dados geográficos carregado no mapa.                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
| Poderá ainda consultar no mapa uma extensão geográfica presente na tabela de limites, para tal basta selecionar a linha em questão e premir o botão                                                                                                                                                                                          |
| |100016320000327000003270A22C429A68005E8D_svg|                                                                                                                                                                                                                                                                                               |
| |10000201000001E8000001E8CCDB88B34D87F801_png|                                                                                                                                                                                                                                                                                               |
| . Se desejar alterar estes limites via o mapa só terá de a desenhar e premir o botão “Alterar”.                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


|100002010000032000000242921984300E64B038_png|
|100002010000032000000242921984300E64B038_png|

+--------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento                 | Obrig. * | Múltiplo | Definição                                                                                                                                             |
|                          |          |          |                                                                                                                                                       |
+--------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Identificador Geográfico | Não      | Sim      | Referência espacial sob a forma de um topónimo ou código que identifica uma localização. Pode conter múltiplos conjuntos dos seguintes sub‑elementos. |
| ^^^^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                                                                       |
|                          |          |          |                                                                                                                                                       |
+--------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Identificador            | Não      | Não      | Código que identifica uma localização, exº NUTS.                                                                                                      |
|                          |          |          |                                                                                                                                                       |
+--------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Contém Recurso           | Não      | Não      | Indica se o retângulo delimitador abrange uma área coberta pelos dados ou uma área onde os dados não estão presentes.                                 |
|                          |          |          |                                                                                                                                                       |
+--------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------+


+-----------------------+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento              | **Obrig. *** | **Múltiplo** | Definição                                                                                                                                   |
|                       |              |              |                                                                                                                                             |
+-----------------------+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Sistema de Referência | Sim          | Sim          | Define o(s) código(s) do(s) sistema(s) de referência de coordenadas sobre o qual o recurso pode ser disponibilizado, a partir de uma lista. |
| ^^^^^^^^^^^^^^^^^^^^^ |              |              |                                                                                                                                             |
|                       |              |              |                                                                                                                                             |
+-----------------------+--------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------+



Informação Temporal
~~~~~~~~~~~~~~~~~~~

Informação geral sobre as referências e extensões temporais do recurso. Contém os seguintes elementos e sub‑elementos:


+---------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------+
| Elemento                                                                                                            | Obrig. * | Múltiplo | Definição                                        |
|                                                                                                                     |          |          |                                                  |
+---------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------+
| Extensão Temporal                                                                                                   | Não      | Não      | Período de tempo para o qual o recurso é válido. |
| ^^^^^^^^^^^^^^^^^                                                                                                   |          |          |                                                  |
|                                                                                                                     |          |          |                                                  |
+---------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------+
| Data de Início                                                                                                      | Não      | Não      | Data e hora de início.                           |
|                                                                                                                     |          |          |                                                  |
+---------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------+
| Data de Fim                                                                                                         | Não      | Não      | Data e hora de fim.                              |
|                                                                                                                     |          |          |                                                  |
+---------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------+
| **Notas**                                                                                                                                                                                    |
| : Para introduzir valores terá de usar o Calendário disponibilizado no respetivo campo.                                                                                                      |
|                                                                                                                                                                                              |
| Para apagar o conteúdo do campo prima o botão                                                                                                                                                |
| |1000000000000010000000108DFD72183B48C685_png|                                                                                                                                               |
|                                                                                                                                                                                              |
| No caso da extensão temporal corresponder a um instante preencha a Data de Início com o mesmo valor da Data de Fim.                                                                          |
|                                                                                                                                                                                              |
| Poderá consultar o intervalo temporal resultante dos valores aqui preenchidos no canto superior direito do ecrã.                                                                             |
|                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


+-----------------------------------------------------------------------------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------+
| Elemento                                                                                | Obrig. *     | Múltiplo | Definição                                                                                                           |
|                                                                                         |              |          |                                                                                                                     |
+-----------------------------------------------------------------------------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------+
| Referência Temporal                                                                     | Sim          | Sim      | Data de referência para o recurso. Este elemento obriga a que pelo menos um dos seus sub‑elementos seja preenchido. |
| ^^^^^^^^^^^^^^^^^^^                                                                     |              |          |                                                                                                                     |
|                                                                                         |              |          |                                                                                                                     |
+-----------------------------------------------------------------------------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------+
| Data de Criação                                                                         | Condi-cional | Não      | Data de referência para a criação do recurso.                                                                       |
|                                                                                         |              |          |                                                                                                                     |
+-----------------------------------------------------------------------------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------+
| Data de Última Revisão                                                                  | Condi-cional | Não      | Data de referência da última revisão efetuada ao recurso.                                                           |
|                                                                                         |              |          |                                                                                                                     |
+-----------------------------------------------------------------------------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------+
| Data de Publicação                                                                      | Condi-cional | Sim      | Data(s) de referência da publicação do recurso.                                                                     |
|                                                                                         |              |          |                                                                                                                     |
+-----------------------------------------------------------------------------------------+--------------+----------+---------------------------------------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                                                                               |
| : Para introduzir valores terá de usar o Calendário disponibilizado no respetivo campo.                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| Para apagar o conteúdo do campo prima o botão                                                                                                                                                                                           |
| |1000000000000010000000108DFD72183B48C685_png|                                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| No caso da Data de Publicação, por permitir vários valores, terá ainda de                                                                                                                                                               |
| premir o botão                                                                                                                                                                                                                          |
| |10000579000029A7000029A7953875AF1C0808FC_svg|                                                                                                                                                                                          |
| |100002010000019300000193BC9FD78E936508CD_png|                                                                                                                                                                                          |
| .                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+





























Qualidade
~~~~~~~~~

Informação relativa à qualidade dos dados, especificada para um dado âmbito ou para o recurso no seu todo. Contém os seguintes elementos e sub‑elementos:


**Elementos referentes ao **
*Histórico*
**:**

+------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento               | Obrig. * | Múltiplo | Definição                                                                                                                                                                                                                                                          |
|                        |          |          |                                                                                                                                                                                                                                                                    |
+------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Declaração (Português) | Sim      | Não      | Descrição geral sobre o conhecimento do produtor sobre o histórico de um recurso. Os processos e fontes de dados devem ser descritos resumidamente. Se desejar particularizar esta informação poderá fazê-lo preenchendo o elemento opcional “Etapas do Processo”. |
| ^^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                                                                                                                                                                                    |
|                        |          |          |                                                                                                                                                                                                                                                                    |
+------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


+---------------------+----------+----------+---------------------------------------------------------------------------------------------------------+
| Elemento            | Obrig. * | Múltiplo | Definição                                                                                               |
|                     |          |          |                                                                                                         |
+---------------------+----------+----------+---------------------------------------------------------------------------------------------------------+
| Declaração (Inglês) | Não      | Não      | Descrição geral sobre o conhecimento do produtor sobre o histórico de um recurso traduzido para Inglês. |
| ^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                         |
|                     |          |          |                                                                                                         |
+---------------------+----------+----------+---------------------------------------------------------------------------------------------------------+


+--------------------+----------+----------+------------------------------------------------------------------------------------------------------------+
| Elemento           | Obrig. * | Múltiplo | Definição                                                                                                  |
|                    |          |          |                                                                                                            |
+--------------------+----------+----------+------------------------------------------------------------------------------------------------------------+
| Etapas do Processo | Não      | Sim      | Descreve os vários processamentos efetuados para a obtenção do recurso.                                    |
| ^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                            |
|                    |          |          |                                                                                                            |
+--------------------+----------+----------+------------------------------------------------------------------------------------------------------------+
| Descrição          | Sim      | Não      | Descrição da etapa do processo efetuado ao conjunto de dados incluindo parâmetros e tolerâncias aplicados. |
|                    |          |          |                                                                                                            |
+--------------------+----------+----------+------------------------------------------------------------------------------------------------------------+
| Data               | Não      | Não      | Data ou Intervalo temporal em que a etapa ocorreu.                                                         |
|                    |          |          |                                                                                                            |
+--------------------+----------+----------+------------------------------------------------------------------------------------------------------------+
| Justificação       | Não      | Não      | Necessidade ou finalidade da etapa do processo.                                                            |
|                    |          |          |                                                                                                            |
+--------------------+----------+----------+------------------------------------------------------------------------------------------------------------+


+-----------------+----------+----------+--------------------------------------------------------------------+
| Elemento        | Obrig. * | Múltiplo | Definição                                                          |
|                 |          |          |                                                                    |
+-----------------+----------+----------+--------------------------------------------------------------------+
| Fonte dos Dados | Não      | Sim      | Informações sobre os dados de origem usados na criação do recurso. |
| ^^^^^^^^^^^^^^^ |          |          |                                                                    |
|                 |          |          |                                                                    |
+-----------------+----------+----------+--------------------------------------------------------------------+


**Elementos referentes ao **
*Relatório*
** (Consistência do Domínio):**

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------+
| Elemento                                                                                                                                                                                                                                                         | Obrig. * | Múltiplo | Definição                                                                                                          |
|                                                                                                                                                                                                                                                                  |          |          |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------+
| Resultado da Conformidade                                                                                                                                                                                                                                        | Sim      | Não      | Informações sobre o resultado da avaliação do valor obtido, contra um nível de qualidade de conformidade indicado. |
| ^^^^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                                                                        |          |          |                                                                                                                    |
|                                                                                                                                                                                                                                                                  |          |          |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------+
| Especificação                                                                                                                                                                                                                                                    | Sim      | Não      | Citação de uma especificação de produto ou requisito de utilização, face à qual os dados estão a ser avaliados.    |
|                                                                                                                                                                                                                                                                  |          |          |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------+
| Data de Especificação                                                                                                                                                                                                                                            | Sim      | Não      | Data de referência da especificação citada.                                                                        |
|                                                                                                                                                                                                                                                                  |          |          |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------+
| Tipo de Data                                                                                                                                                                                                                                                     | Sim      | Não      | Evento usado para a data referenciada, definido a partir de uma lista.                                             |
|                                                                                                                                                                                                                                                                  |          |          |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------+
| Resultado Conforme?                                                                                                                                                                                                                                              | Sim      | Não      | Indicação do resultado de conformidade.                                                                            |
|                                                                                                                                                                                                                                                                  |          |          |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------+
| Explicação                                                                                                                                                                                                                                                       | Não      | Não      | Explicação do significado da conformidade do resultado.                                                            |
|                                                                                                                                                                                                                                                                  |          |          |                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                                                                                                                                                                                                                                                   |
| : Este elemento é um requisito obrigatório da Diretiva INSPIRE.                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| Em caso de desconhecimento pode utilizar a informação recomendada pela Diretiva Inspire premindo o botão “Preencher Automaticamente (INSPIRE)”. Os valores preenchidos serão os seguintes:                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| “                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Especificação*                                                                                                                                                                                                                                                                                                                                                                                             |
| ”: Regulamento (UE) n . o 1089/2010 da Comissão de 23 de Novembro de 2010 que estabelece as disposições de execução da Directiva 2007/2/CE do Parlamento Europeu e do Conselho relativamente à interoperabilidade dos conjuntos e serviços de dados geográficos.                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| “                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Data de Especificação*                                                                                                                                                                                                                                                                                                                                                                                     |
| ”: 2010-12-08                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| “                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Tipo de Data*                                                                                                                                                                                                                                                                                                                                                                                              |
| ”: Publicação                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| “                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Resultado Conforme?*                                                                                                                                                                                                                                                                                                                                                                                       |
| ”: Não (                                                                                                                                                                                                                                                                                                                                                                                                    |
| *checkbox*                                                                                                                                                                                                                                                                                                                                                                                                  |
| desselecionado)                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| “                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Explicação*                                                                                                                                                                                                                                                                                                                                                                                                |
| ”: Ver a norma da especificação                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




Restrições
~~~~~~~~~~

Informação relativa a restrições e pré-requisitos legais e de segurança para o acesso e utilização do recurso. Contém os seguintes elementos e sub‑elementos:


+----------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elemento             | Obrig. * | Múltiplo | Definição                                                                                                                                                                                                                      |
|                      |          |          |                                                                                                                                                                                                                                |
+----------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Restrições Legais    | Sim      | Sim      | Restrições e pré-requisitos legais para acesso e utilização do recurso ou metadado. Pode conter múltiplos conjuntos dos seguintes sub‑elementos.                                                                               |
| ^^^^^^^^^^^^^^^^^    |          |          |                                                                                                                                                                                                                                |
|                      |          |          |                                                                                                                                                                                                                                |
+----------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Limitações ao Uso    | Sim      | Sim      | Pretende descrever as restrições para o acesso e uso do recurso, descrição dos termos e condições incluindo, se aplicável, taxas a pagar ou a indicação                                                                        |
|                      |          |          |                                                                                                                                                                                                                                |
|                      |          |          | de um URL onde essa informação esteja disponível.                                                                                                                                                                              |
|                      |          |          |                                                                                                                                                                                                                                |
|                      |          |          | Indica também se o recurso não é adequado para um tipo específico de utilização por exº: "não deve ser usado para a navegação".                                                                                                |
|                      |          |          |                                                                                                                                                                                                                                |
+----------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Restrições de Acesso | Sim      | Sim      | Restrições de acesso aplicadas ao recurso para assegurar a propriedade intelectual e quaisquer restrições especiais ou limitações sobre a obtenção do recurso. Definido a partir de uma lista. Definido a partir de uma lista. |
|                      |          |          |                                                                                                                                                                                                                                |
|                      |          |          | Se o recurso não tiver restrições de acesso deve ser escolhida a opção "Outras Restrições".                                                                                                                                    |
|                      |          |          |                                                                                                                                                                                                                                |
+----------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Restrições de Uso    | Sim      | Sim      | Constrangimentos aplicados de modo a garantir a proteção da propriedade intelectual do recurso bem como restrições especiais ou limitações e advertências sobre o uso do recurso ou metadados.                                 |
|                      |          |          | Definido a partir de uma lista.                                                                                                                                                                                                |
|                      |          |          |                                                                                                                                                                                                                                |
|                      |          |          | Se o recurso não tiver restrições de uso deve ser escolhida a opção "Outras Restrições".                                                                                                                                       |
|                      |          |          |                                                                                                                                                                                                                                |
+----------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Outras Restrições    | Não      | Sim      | Outras restrições e pré-requisitos legais para aceder e utilizar o recurso ou metadados.                                                                                                                                       |
|                      |          |          |                                                                                                                                                                                                                                |
+----------------------+----------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


+-------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------+
| Elemento                | Obrig. * | Múltiplo | Definição                                                                                                       |
|                         |          |          |                                                                                                                 |
+-------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------+
| Restrições de Segurança | Não      | Sim      | Define as restrições de manuseamento do recurso ou metadados, a partir de uma lista (se aplicável):             |
| ^^^^^^^^^^^^^^^^^^^^^^^ |          |          | *Altamente Secreto*                                                                                             |
|                         |          |          | (do maior nível de segredo);                                                                                    |
|                         |          |          | *Confidencial*                                                                                                  |
|                         |          |          | (disponível para alguém a quem pode ser confiada informação);                                                   |
|                         |          |          | *Não Classificado*                                                                                              |
|                         |          |          | (disponível para divulgação geral);                                                                             |
|                         |          |          | *Restrito*                                                                                                      |
|                         |          |          | (não para divulgação geral);                                                                                    |
|                         |          |          | *Secreto*                                                                                                       |
|                         |          |          | (mantido ou para ser mantido privado, desconhecido, ou oculto para todos a não ser um grupo seleto de pessoas). |
|                         |          |          |                                                                                                                 |
+-------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------+



Distribuição
~~~~~~~~~~~~

Informação relativa ao distribuidor e as alternativas para obtenção do recurso. Contém os seguintes elementos e sub‑elementos:


+-------------------------+----------+----------+----------------------------------------------------------------------------------------------------------------------+
| Elemento                | Obrig. * | Múltiplo | Definição                                                                                                            |
|                         |          |          |                                                                                                                      |
+-------------------------+----------+----------+----------------------------------------------------------------------------------------------------------------------+
| Formato de Distribuição | Sim      | Sim      | O objetivo deste elemento é dar a conhecer o(s) formato(s) em que o recurso se encontra disponível aos utilizadores. |
| ^^^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                                      |
|                         |          |          |                                                                                                                      |
+-------------------------+----------+----------+----------------------------------------------------------------------------------------------------------------------+
| Nome do Formato         | Sim      | Não      | O acrónimo ou extensão por que é conhecido o formato deve, sempre que possível, constar no nome.                     |
|                         |          |          |                                                                                                                      |
+-------------------------+----------+----------+----------------------------------------------------------------------------------------------------------------------+
| Versão                  | Sim      | Não      | Versão do formato,                                                                                                   |
|                         |          |          | caso não se saiba pode                                                                                               |
|                         |          |          | colo                                                                                                                 |
|                         |          |          | car                                                                                                                  |
|                         |          |          | “Não aplicável” ou “Desconhecida”.                                                                                   |
|                         |          |          |                                                                                                                      |
+-------------------------+----------+----------+----------------------------------------------------------------------------------------------------------------------+


+---------------------+----------+----------+--------------------------------------------------------------------------------------------------+
| Elemento            | Obrig. * | Múltiplo | Definição                                                                                        |
|                     |          |          |                                                                                                  |
+---------------------+----------+----------+--------------------------------------------------------------------------------------------------+
| Tamanho do Ficheiro | Não      | Não      | Tamanho estimado de uma unidade no formato de transferência especificado, expressa em MegaBytes. |
| ^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                  |
|                     |          |          |                                                                                                  |
+---------------------+----------+----------+--------------------------------------------------------------------------------------------------+


+-------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------+
| Elemento                                                    | Obrig. *     | Múltiplo | Definição                                                                          |
|                                                             |              |          |                                                                                    |
+-------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------+
| Localizador do Recurso                                      | Condi-cional | Sim      | Informação relativa a fontes                                                       |
| ^^^^^^^^^^^^^^^^^^^^^^                                      |              |          | *online*                                                                           |
|                                                             |              |          | a partir das quais pode se obter o recurso, mais informação, ou aceder ao serviço. |
|                                                             |              |          |                                                                                    |
+-------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------+
| URL                                                         | Condi-cional | Não      | Local para o acesso                                                                |
|                                                             |              |          | *online*                                                                           |
|                                                             |              |          | via um endereço URL /URI ou esquema similar. Se não existir recomenda‑se           |
|                                                             |              |          | p                                                                                  |
|                                                             |              |          | reench                                                                             |
|                                                             |              |          | er                                                                                 |
|                                                             |              |          | -                                                                                  |
|                                                             |              |          | se                                                                                 |
|                                                             |              |          | com um                                                                             |
|                                                             |              |          | *link*                                                                             |
|                                                             |              |          | para um ponto de contacto com mais informação sobre o descarregamento do recurso.  |
|                                                             |              |          |                                                                                    |
+-------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------+
| Função                                                      | Condi-cional | Não      | Define o tipo de recurso, a partir de uma lista.                                   |
|                                                             |              |          |                                                                                    |
|                                                             |              |          | Não se aplica a Serviços.                                                          |
|                                                             |              |          |                                                                                    |
+-------------------------------------------------------------+--------------+----------+------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                  |
| :                                                                                                                                                                          |
| P                                                                                                                                                                          |
| ara os CDG é condicional à existência de um recurso online,                                                                                                                |
| p                                                                                                                                                                          |
| ara Serviços é obrigatório.                                                                                                                                                |
|                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Elemento                                                               | Obrig. * | Múltiplo | Definição                                                                                                             |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Responsáveis pela Distribuição (Contacto)                              | Não      | Sim      | Informações necessárias para permitir o contacto com a pessoa / organização responsável pela distribuição do recurso. |
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                              |          |          | Pode conter múltiplos conjuntos de sub‑elementos:                                                                     |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Nome                                                                   | Não      | Não      | Nome da pessoa responsável.                                                                                           |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Organização                                                            | Sim      | Não      | Nome da organização responsável.                                                                                      |
|                                                                        |          |          |                                                                                                                       |
|                                                                        |          |          | Poderá selecionar de uma Lista de valores ou preencher de forma livre no campo “Outra (                               |
|                                                                        |          |          | N                                                                                                                     |
|                                                                        |          |          | ão                                                                                                                    |
|                                                                        |          |          | L                                                                                                                     |
|                                                                        |          |          | istada)”                                                                                                              |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Morada                                                                 | Não      | Não      | Morada da pessoa ou organização responsável.                                                                          |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Cidade                                                                 | Não      | Não      | Cidade da pessoa ou organização responsável.                                                                          |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Código-Postal                                                          | Não      | Não      | Código-Postal da pessoa ou organização responsável.                                                                   |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| País                                                                   | Não      | Não      | País                                                                                                                  |
|                                                                        |          |          | ** **                                                                                                                 |
|                                                                        |          |          | da pessoa ou organização responsável.                                                                                 |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Telefone                                                               | Não      | Sim      | Número(s) de telefone da organização ou indivíduo.                                                                    |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Fax                                                                    | Não      | Sim      | Número(s) de fax da organização ou indivíduo.                                                                         |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Endereço Eletrónico                                                    | Sim      | Sim      | Endereço(s) Eletrónico(s) da organização ou indivíduo.                                                                |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| Informação                                                             | Não      | Não      | Informação                                                                                                            |
| *Online*                                                               |          |          | *online *                                                                                                             |
|                                                                        |          |          | (endereço URL / URI)                                                                                                  |
|                                                                        |          |          | que pode ser usada como contacto individual ou institucional.                                                         |
|                                                                        |          |          |                                                                                                                       |
+------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                                                            |
| : Este elemento disponibiliza as seguintes funcionalidades / botões:                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| “Adicionar Contacto” Para adicionar um novo contacto.                                                                                                                                                                |
|                                                                                                                                                                                                                      |
| |10000A990000034F0000034F635B68E6E0D88521_svg|                                                                                                                                                                       |
| |100002010000002000000020A3F87039BE9D0D7E_png|                                                                                                                                                                       |
| Para importar um contacto da sua Lista de Contactos para o formulário.                                                                                                                                               |
|                                                                                                                                                                                                                      |
| |1000083700002D5300002D534093D958E24AE6E2_svg|                                                                                                                                                                       |
| |10000201000001B7000001B78F0FC5D379C32E50_png|                                                                                                                                                                       |
| Para guardar o contacto na sua Lista de Contactos.                                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| |1000136C0000026100000261C06770E50C4736EF_svg|                                                                                                                                                                       |
| |100002010000001700000017FBA90A52D3565DE1_png|                                                                                                                                                                       |
| Para remover o contacto.                                                                                                                                                                                             |
|                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+





























Metadados
~~~~~~~~~

Informação relativa aos Metadados. Contém os seguintes elementos e sub‑elementos:


+---------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Elemento                  | Obrig. * | Múltiplo | Definição                                                                                              |
|                           |          |          |                                                                                                        |
+---------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Identificador do Ficheiro | Sim      | Não      | Identificador único do Metadado. Recomenda-se a utilização de um UUID, pode usar o botão “Gerar UUID”. |
| ^^^^^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                        |
|                           |          |          |                                                                                                        |
+---------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+


+--------------------+----------+----------+-------------------------------------------------------+
| Elemento           | Obrig. * | Múltiplo | Definição                                             |
|                    |          |          |                                                       |
+--------------------+----------+----------+-------------------------------------------------------+
| Data dos Metadados | Sim      | Não      | Data de criação do metadado ou da última atualização. |
| ^^^^^^^^^^^^^^^^^^ |          |          |                                                       |
|                    |          |          |                                                       |
+--------------------+----------+----------+-------------------------------------------------------+


+-------------+----------+----------+---------------------------------------------------------------+
| Elemento    | Obrig. * | Múltiplo | Definição                                                     |
|             |          |          |                                                               |
+-------------+----------+----------+---------------------------------------------------------------+
| Codificação | Condi    | Não      | Define a codificação informática de caracteres utilizada no m |
| ^^^^^^^^^^^ | -cional  |          | etadado.                                                      |
|             |          |          | Preencha no caso de ser diferente de “utf8”.                  |
|             |          |          |                                                               |
+-------------+----------+----------+---------------------------------------------------------------+


+----------+----------+----------+------------------------------------------------------------------------------------------------------------+
| Elemento | Obrig. * | Múltiplo | Definição                                                                                                  |
|          |          |          |                                                                                                            |
+----------+----------+----------+------------------------------------------------------------------------------------------------------------+
| Idioma   | Sim      | Não      | Idioma utilizado no documento de metadados. Por definição é “Português”, língua oficial do projeto SNIMar. |
| ^^^^^^   |          |          |                                                                                                            |
|          |          |          |                                                                                                            |
+----------+----------+----------+------------------------------------------------------------------------------------------------------------+


+-----------------------------+----------+----------+---------------------------------------------------------------------------------------------------------------------+
| Elemento                    | Obrig. * | Múltiplo | Definição                                                                                                           |
|                             |          |          |                                                                                                                     |
+-----------------------------+----------+----------+---------------------------------------------------------------------------------------------------------------------+
| Norma e Perfil de Metadados | Sim      | Não      | Perfil de Metadados que define as especificações técnicas sobre as quais os Metadados são construídos.              |
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ |          |          |                                                                                                                     |
|                             |          |          |                                                                                                                     |
+-----------------------------+----------+----------+---------------------------------------------------------------------------------------------------------------------+
| Nome                        | Não      | Não      | Nome da norma de metadados utilizada. Por definição está fixo em “Perfil SNIMar”, perfil oficial do projeto SNIMar. |
|                             |          |          |                                                                                                                     |
+-----------------------------+----------+----------+---------------------------------------------------------------------------------------------------------------------+
| Versão                      | Não      | Não      | Versão do perfil de metadados utilizado. Por definição está fixa na versão mais atual do perfil à data da versão do |
|                             |          |          | *plugin*                                                                                                            |
|                             |          |          | “EditorMetadadosSNIMar”.                                                                                            |
|                             |          |          |                                                                                                                     |
+-----------------------------+----------+----------+---------------------------------------------------------------------------------------------------------------------+


+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Elemento                                                               | Obrig. * | Múltiplo | Definição                                                                                              |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Responsáveis pelos Metadados (Contacto)                                | Não      | Sim      | Informações necessárias para permitir o contacto com a pessoa / organização responsável pelo Metadado. |
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                |          |          | Pode conter múltiplos conjuntos dos seguintes sub‑elementos:                                           |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Nome                                                                   | Não      | Não      | Nome da pessoa responsável.                                                                            |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Organização                                                            | Sim      | Não      | Nome da organização responsável.                                                                       |
|                                                                        |          |          |                                                                                                        |
|                                                                        |          |          | Poderá selecionar de uma Lista de valores ou preencher de forma livre no campo “Outra (                |
|                                                                        |          |          | N                                                                                                      |
|                                                                        |          |          | ão                                                                                                     |
|                                                                        |          |          | L                                                                                                      |
|                                                                        |          |          | istada)”                                                                                               |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Morada                                                                 | Não      | Não      | Morada da pessoa ou organização responsável.                                                           |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Cidade                                                                 | Não      | Não      | Cidade da pessoa ou organização responsável.                                                           |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Código-Postal                                                          | Não      | Não      | Código-Postal da pessoa ou organização responsável.                                                    |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| País                                                                   | Não      | Não      | País                                                                                                   |
|                                                                        |          |          | ** **                                                                                                  |
|                                                                        |          |          | da pessoa ou organização responsável.                                                                  |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Telefone                                                               | Não      | Sim      | Número(s) de telefone da organização ou indivíduo.                                                     |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Fax                                                                    | Não      | Sim      | Número(s) de fax da organização ou indivíduo.                                                          |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Endereço Eletrónico                                                    | Sim      | Sim      | Endereço(s) Eletrónico(s) da organização ou indivíduo.                                                 |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| Informação                                                             | Não      | Não      | Informação                                                                                             |
| *Online*                                                               |          |          | *online *                                                                                              |
|                                                                        |          |          | (endereço URL / URI)                                                                                   |
|                                                                        |          |          | que pode ser usada como contacto individual ou institucional.                                          |
|                                                                        |          |          |                                                                                                        |
+------------------------------------------------------------------------+----------+----------+--------------------------------------------------------------------------------------------------------+
| **Notas**                                                                                                                                                                                             |
| : Este elemento disponibiliza as seguintes funcionalidades / botões:                                                                                                                                  |
|                                                                                                                                                                                                       |
| “Adicionar Contacto” Para adicionar um novo contacto.                                                                                                                                                 |
|                                                                                                                                                                                                       |
| |10000A990000034F0000034F635B68E6E0D88521_svg|                                                                                                                                                        |
| |100002010000002000000020A3F87039BE9D0D7E_png|                                                                                                                                                        |
| Para importar um contacto da sua Lista de Contactos para o formulário.                                                                                                                                |
|                                                                                                                                                                                                       |
| |1000083700002D5300002D534093D958E24AE6E2_svg|                                                                                                                                                        |
| |10000201000001B7000001B78F0FC5D379C32E50_png|                                                                                                                                                        |
| Para guardar o contacto na sua Lista de Contactos.                                                                                                                                                    |
|                                                                                                                                                                                                       |
| |1000136C0000026100000261C06770E50C4736EF_svg|                                                                                                                                                        |
| |100002010000001700000017FBA90A52D3565DE1_png|                                                                                                                                                        |
| Para remover o contacto.                                                                                                                                                                              |
|                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |100002C10000036900000369991FE712D56473BF_svg| image:: images/100002C10000036900000369991FE712D56473BF.svg


.. |100002010000002100000021EFB2E74358139587_png| image:: images/100002010000002100000021EFB2E74358139587.png


.. |10000579000029A7000029A7953875AF1C0808FC_svg| image:: images/10000579000029A7000029A7953875AF1C0808FC.svg


.. |100002010000019300000193BC9FD78E936508CD_png| image:: images/100002010000019300000193BC9FD78E936508CD.png


.. |1000041B000029A6000029A63B246D96BFBDD93A_svg| image:: images/1000041B000029A6000029A63B246D96BFBDD93A.svg


.. |10000201000001930000019328914E2E388B62C5_png| image:: images/10000201000001930000019328914E2E388B62C5.png


.. |10000A990000034F0000034F635B68E6E0D88521_svg| image:: images/10000A990000034F0000034F635B68E6E0D88521.svg


.. |100002010000002000000020A3F87039BE9D0D7E_png| image:: images/100002010000002000000020A3F87039BE9D0D7E.png


.. |1000083700002D5300002D534093D958E24AE6E2_svg| image:: images/1000083700002D5300002D534093D958E24AE6E2.svg


.. |10000201000001B7000001B78F0FC5D379C32E50_png| image:: images/10000201000001B7000001B78F0FC5D379C32E50.png


.. |1000136C0000026100000261C06770E50C4736EF_svg| image:: images/1000136C0000026100000261C06770E50C4736EF.svg


.. |100002010000001700000017FBA90A52D3565DE1_png| image:: images/100002010000001700000017FBA90A52D3565DE1.png


.. |10000000000003A00000027449993894749EB3FE_png| image:: images/10000000000003A00000027449993894749EB3FE.png
    :width: 17.45cm
    :height: 11.811cm


.. |100016320000327000003270A22C429A68005E8D_svg| image:: images/100016320000327000003270A22C429A68005E8D.svg


.. |10000201000001E8000001E8CCDB88B34D87F801_png| image:: images/10000201000001E8000001E8CCDB88B34D87F801.png


.. |10000544000046A9000046A9C576A73C6EFC279A_svg| image:: images/10000544000046A9000046A9C576A73C6EFC279A.svg


.. |10000201000002AC000002AC93F9F67F6B63BBC7_png| image:: images/10000201000002AC000002AC93F9F67F6B63BBC7.png


.. |100005EF0000178100001781273D089BC013EA25_svg| image:: images/100005EF0000178100001781273D089BC013EA25.svg


.. |10000201000000E3000000E3D57FEACA303168F9_png| image:: images/10000201000000E3000000E3D57FEACA303168F9.png


.. |1000055D000017810000178195ACBD3347489439_svg| image:: images/1000055D000017810000178195ACBD3347489439.svg


.. |10000201000000E3000000E3A255E6F26DADD695_png| image:: images/10000201000000E3000000E3A255E6F26DADD695.png


.. |1000050E00002ADA00002ADA3CBB09F56AF59D9E_svg| image:: images/1000050E00002ADA00002ADA3CBB09F56AF59D9E.svg


.. |100002010000019F0000019F2E58215D7D78FD03_png| image:: images/100002010000019F0000019F2E58215D7D78FD03.png


.. |100002010000001C0000001A19ADBB8A5C169711_png| image:: images/100002010000001C0000001A19ADBB8A5C169711.png
    :width: 0.741cm
    :height: 0.688cm


.. |100002010000032000000242921984300E64B038_png| image:: images/100002010000032000000242921984300E64B038.png
    :width: 18.009cm
    :height: 13.106cm


.. |1000000000000010000000108DFD72183B48C685_png| image:: images/1000000000000010000000108DFD72183B48C685.png
    :width: 0.423cm
    :height: 0.423cm



