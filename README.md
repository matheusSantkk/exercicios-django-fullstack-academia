Levantamento de requisitos — Academia Corpo em Movimento
Documento 01 · versão 1.0 · 21/10/2026 Cliente: Renata Albuquerque, proprietária · Analista: Carlos Celestino · Equipe de
desenvolvimento: a sua

1. Contexto
   A Academia Corpo em Movimento funciona há seis anos em Caruaru e oferece aulas de musculação, pilates, natação e funcional.
   Hoje a grade de horários é um quadro branco na recepção e uma foto dele no WhatsApp. Toda vez que muda um horário ou entra
   um instrutor novo, a foto fica desatualizada e os alunos ligam para confirmar.
   Nas palavras da cliente, na reunião de levantamento:
   "Eu quero duas coisas. Um lugar onde eu mesma cadastro as modalidades e as turmas, sem depender de ninguém, e que
   consiga achar rápido a turma de um instrutor ou só as turmas de pilates. E um site simples onde o aluno vê o que a academia
   oferece e a grade da semana, sempre certa, porque sai direto do que eu cadastrei."
2. Objetivo
   Construir um sistema web com painel administrativo para a proprietária manter modalidades e turmas, e duas páginas públicas
   que mostram essas informações aos alunos, lidas diretamente do banco de dados.
3. Escopo
   Entra nesta versão: cadastro de modalidades e turmas pelo painel; página inicial com as modalidades; página com a grade de
   turmas; filtros e busca no painel.
   Não entra nesta versão: matrícula de alunos, pagamento, login de aluno, aplicativo de celular, fotos.
4. Requisitos funcionais
   Código Requisito
   RF01 O sistema deve permitir cadastrar, editar, consultar e excluir modalidades pelo painel administrativo.
   RF02 O sistema deve permitir cadastrar, editar, consultar e excluir turmas pelo painel administrativo.
   RF03 No painel, a lista de turmas deve mostrar, em colunas: modalidade, dia da semana, horário, instrutor e vagas.
   RF04 No painel, deve ser possível filtrar as turmas por modalidade e por dia da semana, e buscar turmas pelo nome do instrutor.
   RF05 No painel, a lista de modalidades deve mostrar o nome e se está ativa, com filtro por ativa/inativa.
   RF06 A página inicial ( / ) deve mostrar o nome da academia, endereço, telefone e a lista das modalidades ativas com a descrição de cada
   uma.
   RF07 A página de grade ( /turmas/ ) deve mostrar todas as turmas em uma tabela com modalidade, dia, horário, instrutor e vagas,
   ordenadas por dia da semana e horário.
   RF08 As duas páginas devem ter um menu com link para a outra.
5. Regras de negócio
   Programador Full Stack · Senac PE · Prof. Carlos Celestino 1 / 3
   Código Regra
   RN01 Toda turma pertence a exatamente uma modalidade. Uma modalidade pode ter várias turmas.
   RN02 Não pode existir turma sem modalidade.
   RN03 Não deve ser possível excluir uma modalidade que ainda tenha turmas cadastradas.
   RN04 O dia da semana é escolhido de uma lista fixa: segunda a sábado. Não é texto livre.
   RN05 O horário é informado no formato 24h (ex.: 07:30 , 18:00 ).
   RN06 Vagas é um número inteiro, nunca negativo.
   RN07 Não podem existir duas modalidades com o mesmo nome.
   RN08 Modalidade inativa continua no painel, mas não aparece na página inicial.
6. Dados
   Modalidade
   Campo Tipo Obrigatório Observação
   nome texto curto sim único (RN07)
   descrição texto longo não aparece na página inicial
   ativa sim/não sim padrão: sim
   Turma
   Campo Tipo Obrigatório Observação
   modalidade referência a uma Modalidade sim RN01, RN02, RN03
   dia da semana lista fixa sim RN04
   horário hora sim RN05
   instrutor texto curto sim nome da pessoa
   vagas inteiro não negativo sim padrão: 10 (RN06)
   Em todo lugar em que uma turma for exibida (painel ou página), ela deve ser identificada de forma legível, por exemplo: Pilates —
   Segunda 07:30 .
7. Dados iniciais
   Para a entrega, o sistema deve estar carregado com estes dados, cadastrados pelo painel:
   Modalidade Descrição Ativa
   Musculação Treino com pesos, acompanhamento individual sim
   Pilates Solo e aparelhos, turmas pequenas sim
   Funcional Circuito de alta intensidade sim
   Natação Piscina aquecida (em reforma) não
   Modalidade Dia Horário Instrutor Vagas
   Pilates Segunda 07:30 Rafael 8
   Musculação Segunda 19:00 Carla 15
   Funcional Terça 06:30 Diego 12
   Musculação Terça 18:00 Carla 15
   Pilates Quarta 07:30 Rafael 8
   Funcional Sábado 09:00 Diego 20
   Programador Full Stack · Senac PE · Prof. Carlos Celestino 2 / 3
8. Requisitos não funcionais
   Código Requisito
   RNF01 Python 3 e Django; banco de dados padrão do Django (SQLite).
   RNF02 Projeto novo, criado do zero, em ambiente virtual próprio.
   RNF03 Código em repositório no GitHub, com .gitignore (venv, **pycache** , db.sqlite3 ) e pelo menos três commits com
   mensagens que digam o que foi feito: projeto criado; modelos e painel; páginas.
   RNF04 README.md com: nome da equipe, como rodar o projeto, e o diário de IA do dia.
   RNF05 Qualquer decisão que o documento não cobre deve ser tomada pela equipe e registrada no README, em uma seção "Decisões".
9. Critérios de aceite
   A entrega é aceita quando o analista, no computador da equipe, consegue:
   [ ] entrar no painel e ver as duas listas (modalidades e turmas) com as colunas pedidas;
   [ ] filtrar as turmas por modalidade e por dia; buscar por "Carla" e achar as duas turmas dela;
   [ ] tentar excluir a modalidade Musculação e ser impedido (RN03);
   [ ] abrir / e ver as três modalidades ativas com descrição, e não ver Natação;
   [ ] abrir /turmas/ e ver as seis turmas na ordem: segunda 07:30, segunda 19:00, terça 06:30, terça 18:00, quarta 07:30,
   sábado 09:00;
   [ ] navegar de uma página para a outra pelo menu;
   [ ] abrir o repositório no GitHub e ver os três commits e o README.
10. Entrega
    Prazo: fim do encontro de hoje.
    Forma: link do repositório + demonstração de 5 minutos para o analista.
    Depois da entrega há uma segunda etapa, que será apresentada na hora.
    Programador Full Stack · Senac PE · Prof. Carlos Celestino 3 / 3

## Equipe

- Matheus

## Como executar

1. Crie e ative um ambiente virtual: `python -m venv venv` e `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows).
2. Instale as dependências com `pip install -r requirements.txt`.
3. Execute `python manage.py migrate`.
4. Crie um usuário administrativo com `python manage.py createsuperuser`.
5. Inicie o servidor com `python manage.py runserver`.
6. Preencha o banco sql com `env\Scripts\python.exe manage.py test academia` (Windows) 
7. Acesse `/` para ver as modalidades, `/turmas/` para a grade e `/admin/` para administrar os dados.

## Decisões

- O endereço e o telefone da academia aparecem como placeholders até que os dados reais sejam fornecidos.
- A ordem dos dias da semana é definida explicitamente de segunda a sábado, seguida pelo horário.
- A interface e os horários usam português do Brasil e o fuso `America/Recife`.
- A matrícula de alunos foi removida para manter esta versão dentro do escopo definido no levantamento.
- Os dados de demonstração do SQLite correspondem aos dados iniciais do levantamento; eles são mantidos no banco local do projeto.
- O diário de IA não foi registrado, conforme orientação do responsável pelo projeto.
