# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Conventional Commits

Este projeto segue o padrão de Conventional Commits para mensagens de commit. Cada mensagem de commit deve ser estruturada da seguinte forma:

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

### Tipos de Commit

- `feat`: Uma nova funcionalidade
- `fix`: Uma correção de bug
- `docs`: Alterações em documentação
- `style`: Alterações que não afetam o código (espaços, formatação, etc)
- `refactor`: Alterações de código que não corrigem bugs nem adicionam funcionalidades
- `perf`: Alterações de código que melhoram performance
- `test`: Adição ou correção de testes
- `chore`: Alterações em arquivos de build, ferramentas, etc

### Exemplos

```bash
# Nova funcionalidade
feat(assignments): adiciona sistema de pontuação em exercícios

# Correção de bug
fix(templates): corrige renderização de código em blocos markdown

# Documentação
docs: atualiza instruções de instalação no README

# Refatoração
refactor(assets): reorganiza estrutura de arquivos CSS

# Testes
test(assignments): adiciona testes para validação de submissões

# Múltiplos escopos
feat(assignments,templates): implementa novo formato de exercícios
```

