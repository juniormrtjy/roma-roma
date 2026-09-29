# Verificação da primeira versão

Revisão em 23/09/2026, em navegador Chromium da prévia local.

## Concluído

- HTML: tags aninhadas corretamente, IDs únicos, exatamente um H1, âncoras internas existentes, labels associados aos campos e imagens com alt e dimensões.
- Arquivos: referências locais de imagens, CSS, JavaScript e favicon existentes; imagens carregadas na prévia.
- JavaScript: sintaxe validada e console do navegador sem erros ou avisos durante os testes.
- Responsividade: larguras de 1440, 1280, 1024, 768, 480 e 375 px verificadas, sem rolagem horizontal do documento.
- Inspeção visual de abertura, serviços, projetos e formulário/dialog em desktop e celular.
- Menu mobile: abertura, estado `aria-expanded`, fechamento por Escape e navegação por link.
- Formulário vazio: validação nativa bloqueia o rascunho e direciona ao primeiro campo inválido.
- Formulário preenchido com dados fictícios: prepara mensagem com serviço selecionado, sem envio externo.
- Dialog: conteúdo de revisão, cópia confirmada, fechamento por Escape e retorno de foco ao botão de origem.
- Projetos: detalhes expansíveis abrem e mostram o conteúdo pendente, sem apresentar um case inventado como concluído.
- SEO: JSON-LD parseável, sitemap XML válido, robots presente e placeholders de domínio/imagem social identificados.
- Animação: implementação revisada para não ativar a revelação com movimento reduzido; CSS também desativa transições nessa preferência.
- Contatos: telefone, e-mail e Instagram conferidos com a página 28 do PDF; links montados com esses dados.
- Conteúdo principal e navegação existem no HTML, sem dependência de renderização por JavaScript. Sem JS, o botão de rascunho permanece desativado e os contatos diretos continuam disponíveis.

## Limites da verificação

- Não foram enviados e-mails ou mensagens reais; não houve teste de entrega para a caixa da empresa.
- Não foram executados Lighthouse, medição de Core Web Vitals em produção, auditoria automatizada WCAG completa ou teste com leitor de tela/dispositivo físico. Acessibilidade foi revisada na estrutura, nos controles e nas interações descritas acima.
- A preferência por movimento reduzido foi revisada no código; não foi emulada no navegador de teste.
- O projeto não depende de servidor para conteúdo e navegação, mas a abertura de URL `file://` foi bloqueada pela política do navegador de automação. A execução foi testada por HTTP local; a abertura direta do `index.html` deve ser conferida no navegador do usuário. A cópia automática pode exigir contexto seguro, por isso há alternativa de seleção manual.
- Não há URL publicada: o conector nativo de hospedagem Sites não estava disponível.
- Os arquivos públicos somam aproximadamente 480 KB, incluindo variantes de logo que ainda não são usadas. Não há fontes remotas ou bibliotecas de terceiros.

## Antes da publicação definitiva

1. Inserir domínio confirmado em canonical, Open Graph, sitemap e robots.
2. Substituir o placeholder de imagem social por URL e arquivo reais.
3. Completar fotos e dados dos cases; remover legendas de conteúdo pendente correspondentes.
4. Confirmar a atualidade de contatos e do tempo de atuação com a empresa.
5. Revisar o aviso de privacidade se a hospedagem ou novas integrações tratarem dados adicionais.
