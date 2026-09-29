from pathlib import Path
p=Path('index.html');s=p.read_text(encoding='utf-8')
start=s.index('      <!-- PROJETOS '); end=s.index('      <section class="process',start)
s=s[:start]+'''      <!-- PROJETOS — fotografias enviadas pelo usuário em 29/09/2026.
           Os títulos descrevem frentes de atuação; não são nomes oficiais de cases.
           COMPLETAR CASES: inserir cliente contratante, local, data e resultados somente após confirmação. -->
      <section class="projects section container" id="projetos" aria-labelledby="projects-title">
        <div class="section-heading" data-reveal>
          <div>
            <p class="eyebrow">03 / Nossa atuação na prática</p>
            <h2 id="projects-title">Da marca ao encontro.<br>Do encontro à experiência.</h2>
          </div>
          <p>Registros de degustação, exposição de produtos e presença no varejo. Experiências que acontecem de perto.</p>
        </div>
        <div class="project-grid">
          <!-- ADICIONAR NOVO PROJETO: duplique um article; mantenha IDs exclusivos nos details. -->
          <article class="project-card project-wide">
            <figure class="photo-slot project-photo project-photo-complete">
              <img class="replaceable-photo" src="assets/images/projeto-01.jpg" alt="Expositor de sucos Bebah e snacks em uma ponta de gôndola de supermercado" width="960" height="1280" loading="lazy">
            </figure>
            <div class="project-heading">
              <div>
                <p class="eyebrow">Varejo / Exposição de produtos</p>
                <h3>O cuidado no ponto de venda</h3>
              </div>
              <span class="project-index" aria-hidden="true">01</span>
            </div>
            <p class="project-description">Produtos organizados em uma ponta de gôndola, com exposição frontal e identificação de preços.</p>
          </article>
          <article class="project-card project-tasting">
            <figure class="photo-slot project-photo">
              <img class="replaceable-photo" src="assets/images/projeto-02.jpg" alt="Apresentação de bebidas Weber Haus em um balcão de degustação com consumidoras" width="1086" height="1448" loading="lazy">
            </figure>
            <div class="project-heading">
              <div>
                <p class="eyebrow">Experimentação / Degustação</p>
                <h3>Uma experiência para descobrir</h3>
              </div>
              <span class="project-index" aria-hidden="true">02</span>
            </div>
            <p class="project-description">Apresentação de bebidas Weber Haus em um balcão de degustação, com interação no ponto de venda.</p>
            <details id="projeto-degustacao">
              <summary>Ver outro registro</summary>
              <figure class="project-gallery-single">
                <img src="assets/images/weber-haus-registro-pdv.jpg" alt="Duas pessoas com garrafas de bebida Weber Haus em um supermercado" width="1086" height="1448" loading="lazy">
                <figcaption>Registro com produtos Weber Haus no ponto de venda.</figcaption>
              </figure>
            </details>
          </article>
          <article class="project-card project-third">
            <figure class="photo-slot project-photo">
              <img class="replaceable-photo" src="assets/images/projeto-03.jpg" alt="Vista lateral de prateleiras com azeites e outros produtos organizados no supermercado" width="899" height="1599" loading="lazy">
            </figure>
            <div class="project-story">
              <div class="project-heading">
                <div>
                  <p class="eyebrow">Merchandising / Gôndolas</p>
                  <h3>Presença em cada detalhe</h3>
                </div>
                <span class="project-index" aria-hidden="true">03</span>
              </div>
              <p class="project-description">A exposição dos produtos vista de perto: organização das prateleiras, rótulos à vista e presença no varejo.</p>
              <details id="projeto-exposicao" open>
                <summary>Ver outros ângulos</summary>
                <div class="project-gallery">
                  <figure>
                    <img src="assets/images/gondola-azeites-lateral.jpg" alt="Detalhe lateral da exposição de azeites nas prateleiras" width="899" height="1599" loading="lazy">
                    <figcaption>Detalhes da exposição.</figcaption>
                  </figure>
                  <figure>
                    <img src="assets/images/gondola-azeites-frontal.jpg" alt="Vista frontal da gôndola de azeites, com identificação de preços e registro da visita na própria fotografia" width="960" height="1280" loading="lazy">
                    <figcaption>Vista frontal do ponto de venda.</figcaption>
                  </figure>
                </div>
              </details>
            </div>
          </article>
        </div>
      </section>
''' +s[end:]
p.write_text(s,encoding='utf-8')
