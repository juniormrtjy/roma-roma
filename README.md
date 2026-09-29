# ROMANEIRO — site institucional

Site estático em HTML5, CSS3 e JavaScript puro. Não precisa de Node, npm, frameworks ou compilação. Abra `index.html` diretamente ou sirva esta pasta com um servidor estático. Fontes do sistema evitam dependências externas.

## Estrutura entregue

```text
index.html                 Conteúdo, contatos, formulário, SEO e dados estruturados
css/style.css              Visual, cores, layouts, animações e responsividade
js/script.js               Menu, revelações, rascunho de mensagem, dialog e ano
assets/images/             Logos oficiais otimizadas e imagens substituíveis
assets/icons/favicon.png   Símbolo oficial da marca em tamanho pequeno
robots.txt                 Instruções de indexação
sitemap.xml                Home (única página pública)
docs/conteudo-e-fontes.md   Inventário do PDF e decisões editoriais
docs/verificacao.md         Verificações feitas e limitações
README.md                  Este guia
```

`tmp/` contém somente material de trabalho e renderizações do PDF. Não envie essa pasta para a hospedagem. Os scripts de preparação não fazem parte do funcionamento do site.

## Edição rápida

| O que mudar | Onde |
|---|---|
| Cores, largura e espaçamentos | `css/style.css`, bloco `:root` no início |
| Tipografia | variável `--font`; escalas de `h1`, `h2`, `h3` e media queries |
| Textos | diretamente em `index.html`, por seção comentada |
| Telefone e WhatsApp | contatos e rodapé em `index.html`; atualizar também `telephone` no JSON-LD |
| Número do WhatsApp | `wa.me/5521996190811`: código do país + DDD + número, somente dígitos |
| E-mail | contato, rodapé, privacidade e JSON-LD em `index.html`; `contactEmail` em `js/script.js` |
| Instagram | links de contato/rodapé e `sameAs` no JSON-LD de `index.html` |
| Serviços | adicionar/remover `article.service-card` dentro de `.service-grid`; atualizar o `select#servico` e o rodapé se necessário |
| Projetos | adicionar/remover `article.project-card` dentro de `.project-grid`; ajustar imagens, textos e IDs exclusivos de `details` |
| Clientes | `.client-grid` e `.client-list`; incluir apenas marcas verificadas |
| Domínio/SEO | head de `index.html`, `robots.txt` e `sitemap.xml` |

Busque pelos comentários `ALTERAR`, `TROCAR`, `ADICIONAR`, `INSERIR` e `COMPLETAR` para encontrar pontos de manutenção.

## Substituir as fotografias

Os JPGs abaixo já existem e são placeholders gráficos próprios, sem imagens de banco, terceiros ou cases inventados. Basta sobrescrever o arquivo com uma fotografia real e recarregar a página. Nenhum efeito depende da imagem original. A foto ocupa o mesmo espaço com `object-fit: cover`.

| Arquivo em `assets/images/` | Uso | Sugestão |
|---|---|---|
| `hero-romaneiro.jpg` | Destaque de abertura | Retrato, aproximadamente 1000 × 1080 |
| `sobre-romaneiro.jpg` | Sobre a agência | Quadrada ou retrato, pelo menos 1000 px |
| `projeto-01.jpg` | Primeiro projeto / PDV | Paisagem, pelo menos 1200 px |
| `projeto-02.jpg` | Segundo projeto / degustação | Paisagem, pelo menos 1200 px |
| `projeto-03.jpg` | Terceiro projeto / exposição | Paisagem ampla, pelo menos 1200 px |

Também atualize o `alt` da imagem para descrever a fotografia real. Hoje o hero e a imagem de sobre são decorativos (`alt=""`). Nos projetos, remova a legenda “FOTOGRAFIA EM BREVE” e a nota “Portfólio em atualização” quando houver conteúdo aprovado. Complete o nome, cliente, ano e descrição dentro de cada `details`. Se quiser mudar o ponto de recorte, use `object-position` no seletor da foto. Evite texto importante nas fotos, pois o recorte varia com a tela.

As logos foram reduzidas proporcionalmente a partir dos PNGs oficiais, mantendo cores e transparência. Os arquivos originais enviados não foram alterados. Não substitua as logos por texto.

## O que faz o JavaScript

### Slideshow da abertura

A abertura alterna três imagens com fade suave a cada 5 segundos. Para trocar as fotos, substitua `assets/images/hero-romaneiro.jpg`, `assets/images/hero-romaneiro-02.jpg` e `assets/images/hero-romaneiro-03.jpg`. Prefira fotos verticais de aproximadamente 1000 × 1080 px e atualize os textos `alt` no HTML. Os arquivos atuais são apenas composições gráficas, não fotografias de eventos.

Os botões permitem voltar, avançar e pausar. A navegação manual interrompe a troca automática; use “Reproduzir” para retomá-la. Há pausa temporária com o mouse sobre a área, quando ela sai da tela e quando a aba fica oculta. A preferência por movimento reduzido desativa o automático e a transição. Sem JavaScript, aparece a primeira imagem. Para adicionar uma foto, duplique um `img.hero-slide` no HTML; a contagem se ajusta automaticamente. Edite `slideInterval` na seção 05 de `js/script.js` para mudar os 5000 ms.

1. **Menu mobile:** abre/fecha, atualiza `aria-expanded`, fecha por Escape, clique externo, navegação e mudança para desktop. Sem JS, a navegação continua disponível.
2. **Revelações:** usa `IntersectionObserver` em elementos com `data-reveal`; não ativa a animação com preferência por movimento reduzido. Não renderiza conteúdo principal.
3. **Formulário:** usa validação nativa, prepara um rascunho em memória e abre um `dialog` nativo. “Copiar mensagem” usa a área de transferência, com seleção manual como alternativa. “Abrir no meu e-mail” é um link `mailto:`: requer aplicativo de e-mail configurado e depende dele para enviar. Mensagens muito longas podem exceder o limite do aplicativo; nesse caso copie o texto. **Nada é enviado automaticamente e nenhum sucesso de envio é simulado.**
4. **Ano:** atualiza somente o copyright; não calcula nem altera o tempo de atuação.

O dialog fecha pelo botão, Escape ou clique fora da caixa e utiliza o comportamento nativo de foco. Os detalhes dos projetos, clientes adicionais e privacidade usam `details` e `summary`, sem JS.

## Conteúdo que ainda precisa ser confirmado

- Fotografias de hero, equipe e projetos.
- Nome, cliente, data, descrição e resultados de cada case. As categorias atuais vêm do PDF; os títulos são editoriais, não nomes oficiais de projetos.
- Domínio definitivo.
- Imagem de compartilhamento aprovada. As tags sociais contêm um placeholder explícito; o arquivo de imagem social não foi inventado.
- Atualização do dado “mais de 5 anos”: reproduz o material recebido, sem presumir um ano de fundação.
- Política final de privacidade e tratamento das mensagens pela empresa, especialmente se incluir envio por servidor, métricas ou publicidade. O aviso atual descreve o comportamento da versão estática.
- Endereço físico, caso deseje divulgá-lo. O PDF só confirma a área de atuação; não há endereço fictício no site.

Telefone, WhatsApp, e-mail e Instagram já estão preenchidos com os dados do PDF. Não dependem de placeholders.

## SEO e publicação

- Título descritivo, descrição, um H1, headings, conteúdo no HTML, canonical, Open Graph, Twitter Card, favicon, robots e sitemap estão preparados.
- Troque **todas** as ocorrências de `https://SEU-DOMINIO.com.br/` antes da publicação pública. Não deduza o domínio do site a partir do e-mail.
- Troque `INSERIR-IMAGEM-SOCIAL.jpg` por uma imagem real e aprovada, com URL absoluta, nas tags Open Graph e Twitter.
- O JSON-LD `Organization` usa somente dados confirmados. Depois de definir o domínio, acrescente `url` e `logo` absolutos. Pode incluir um bloco `WebSite` com nome e URL então. Não foi inventado endereço para usar `LocalBusiness`.
- `robots.txt` permite indexação, como solicitado. Caso publique uma prévia pública ainda com placeholders, restrinja a indexação dessa prévia na hospedagem até concluir o conteúdo; mantenha a versão final indexável.
- O site não inclui analytics, cookies próprios, pixels, trackers ou fontes externas. A hospedagem poderá registrar requisições conforme a política do provedor.
- Para hospedagem estática, publique `index.html`, `css/`, `js/`, `assets/`, `robots.txt` e `sitemap.xml`. Não há backend nem comandos de build.
- A publicação pelo conector Sites não foi possível nesta sessão: as ferramentas nativas de criação e publicação não estavam disponíveis. O projeto é independente desse serviço e pode ser hospedado em qualquer servidor estático.

## Evolução

Não foram criadas páginas extras, timeline histórica, métricas de eventos/clientes ou depoimentos sem base documental. Para criar novas páginas, reutilize header/footer e CSS, mas defina title, description, canonical e H1 próprios; atualize sitemap e navegação. Um backend futuro deve validar entradas no servidor, prevenir spam e informar envio real; o ponto de integração está comentado em `js/script.js`.
