# Plugin para QGIS 3.x para criação e edição de metadados segundo o perfil SNIMar


**FICHA TÉCNICA VERSÃO PARA QGIS 3.x**

TÍTULO: Manual de Utilizador do Plugin para QGIS 3.x para criação e edição de metadados segundo o perfil SNIMar

AUTORIA: Projecto MARSW e INFORBIOMARES

EMAIL: jgoncal@ualg.pt

DATA: Julho 2020

VERSÃO: 3.x


**CONTACTOS VERSÃO PARA QGIS 3.x**

Projecto MARSW

Telefone: +351289800051

E-mail: jgoncal@ualg.pt

Projecto INFORBIOMARES

Telefone: +351 289 800 051

E-mail: ccmar@ualg.pt


**FICHA TÉCNICA ORIGINAL**

TÍTULO: Manual de Utilizador / Instalação do Editor de Metadados SNIMar

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
é o "*porting*" para a versão 3.x do *software* SIG “QGIS” do editor de Metadados desenvolvido no âmbito do Projecto SNIMar com o objectivo de ser a ferramenta destinada à criação dos metadados em conformidade com o Perfil de Metadados SNIMar. **O trabalho de migração do código para QGIS 3.x foi realizado no âmbito dos projectos MARSW e INFORBIOMARES**.

**Editor de Metadados SNIMar**
foi desenvolvido no âmbito do Projeto SNIMar (http://editor.snimar.pt/)  com o objetivo de ser a ferramenta destinada à criação de metadados em conformidade com o Perfil de Metadados SNIMar. O Editor consiste num *plugin* para a aplicação QGIS, permitindo que a criação de metadados seja feita em paralelo e em simultâneo com a criação e edição de Conjuntos de Dados Geográficos (CDG).

O SNIMar é um projeto nacional, financiado pelo Mecanismo Financeiro do Espaço Económico Europeu 2009-2014 no âmbito dos European Economic Area Grants (EEA Grants), que tem por objetivo o desenvolvimento de uma infraestrutura de dados espaciais marinhos para o aumento da capacidade de avaliação e previsão do estado ambiental das águas marinhas. Esta infraestrutura traduz-se num Geoportal que irá potenciar a interação do público com a informação disponibilizada pelos parceiros e entidades participantes do projeto e constituirá um ponto central de agregação, pesquisa e distribuição de informação geográfica sobre o ambiente marinho em Portugal.

Os metadados de informação geográfica não são mais do que uma descrição textual, de forma normalizada, da informação geográfica. A sua documentação é indispensável para a identificação e avaliação técnica (escala, sistema de referência, qualidade, extensão geográfica e temporal, contactos dos responsáveis) dos CDG, assim como aspetos ligados ao acesso e utilização de serviços de informação geográfica. Pesquisas feitas em sistemas de informação, infraestruturas de dados espaciais (IDE) ou sistemas de comércio eletrónico, são suportadas pelos metadados, que funcionam como o “combustível” para encontrar os recursos desejados.

O Perfil de Metadados SNIMar, definido no âmbito do referido projeto, respeita os requisitos da
Diretiva INSPIRE (Diretiva n.º 2007/2/CE, do Parlamento Europeu e do Conselho, de 14 de março) e as respetivas disposições de execução definidas no Regulamento (CE) n.º 1205/2008 da Comissão, de 3 de dezembro, que estabelece os requisitos aplicáveis à criação e manutenção de metadados para conjuntos de dados geográficos (CDG), séries de conjuntos de dados geográficos e serviços de dados geográficos correspondentes aos temas enumerados nos anexos I, II e III da Diretiva 2007/2/CE. É também importante realçar que o Perfil de Metadados SNIMar teve por base o Perfil Nacional de Metadados de Informação Geográfica (Perfil MIG), que “tem como objetivo principal clarificar aspetos ligados à implementação da produção, gestão e disseminação dos metadados em Portugal, de forma a assegurar a correta caracterização dos recursos geográficos e a sua harmonização com a infraestrutura de informação geográfica portuguesa (SNIG) e europeia (INSPIRE).” [Perfil MIG, 2010], ajustando-se este perfil à realidade nacional dos dados relativos ao ambiente marinho.


Instalação
==========

O
*plugin *
**EditorMetadadosMarswInforbiomares**
* *
foi desenvolvido para operar nos sistemas operativos Linux, Windows
e macOS
e pode ser instalado na aplicação QGIS da seguinte forma:


*   Abrir a aplicação QGIS,
    recomenda-se a utilização d
    a versão 3.10



*   No Menu Principal selecionar
    **Módulos > Gerir e Instalar Módulos**
    .



*   Selecionar o separador
    **Configurações**
    .



*   Adicionar um novo repositório de módulos, premindo o botão “Adicionar...”, e preencher os campos do formulário com os seguintes parâmetros:

    *   *Nome*
        : Editor Metadados Marsw/Inforbiomares



    *   *URL*
        :
        `https://marsw.ualg.pt/static/qgis/editormetadadosmarswinforbiomares.xml <https://marsw.ualg.pt/static/qgis/editormetadadosmarswinforbiomares.xml>`_




    *   *Parâmetros*
        : manter pré-definições



    *   *Ativado*
        : manter pré-definições





*   Fazer “Ok” e a
    tualizar os repositórios premindo o botão “Atualizar todos os repositórios”.



*   Selecionar o separador
    **Não instalado**
    e
    pesquisar por “
    MarSW” ou “Inforbiomares” ou
    “SNIMar”



*   Instalar o
    *p*
    lugin
    através do botão
    “Instalar módulo”.



O
*plugin*

**EditorMetadadosMarswInforbiomares**
ficará ativo e disponível no menu de ferramentas
através do ícone
