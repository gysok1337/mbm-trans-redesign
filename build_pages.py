# -*- coding: utf-8 -*-
"""Generate redesigned inner pages with shared header/footer/nav."""

ICON = {
 'arrow':'<svg class="icon" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>',
 'truck':'<svg class="icon" viewBox="0 0 24 24"><path d="M10 17h4V5H2v12h3"/><path d="M20 17h2v-3.34a4 4 0 0 0-1.17-2.83L19 9h-5v8h1"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>',
 'shield':'<svg class="icon" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
 'clock':'<svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 'pin':'<svg class="icon" viewBox="0 0 24 24"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
 'phone':'<svg class="icon" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>',
 'mail':'<svg class="icon" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
 'chev':'<svg class="icon" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>',
 'doc':'<svg class="icon" viewBox="0 0 24 24"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v5h5"/><path d="M9 13h6M9 17h4"/></svg>',
 'box':'<svg class="icon" viewBox="0 0 24 24"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>',
 'crane':'<svg class="icon" viewBox="0 0 24 24"><path d="M2 22V12a2 2 0 0 1 2-2h2"/><path d="m6 10 4-7 6 3-3 6"/><path d="M14 14h6v6a2 2 0 0 1-2 2H6"/><circle cx="6" cy="18" r="2"/></svg>',
 'train':'<svg class="icon" viewBox="0 0 24 24"><rect x="4" y="3" width="16" height="14" rx="2"/><path d="M4 11h16"/><path d="m8 19-2 3"/><path d="m18 22-2-3"/><circle cx="8.5" cy="14" r="1"/><circle cx="15.5" cy="14" r="1"/></svg>',
}

NAV = [
 ('О компании','o-kompanii.html',None),
 ('Услуги','kontejnernyie-perevozki.html',[
    ('Контейнерные перевозки','kontejnernyie-perevozki.html','box'),
    ('Перевозка негабаритных грузов','perevozka-negabaritnyix-gruzov.html','truck'),
    ('Техника в аренду','texnika-v-arendu.html','crane'),
    ('Ж/Д перевозки','zhd-perevozki.html','train'),
 ]),
 ('Наши проекты','nashi-proektyi.html',None),
 ('Клиенты','nashi-klientyi.html',None),
 ('Контакты','kontaktyi.html',None),
]
SERVICE_PAGES = {'kontejnernyie-perevozki.html','perevozka-negabaritnyix-gruzov.html','texnika-v-arendu.html','zhd-perevozki.html'}

def nav_html(active):
    out=['<nav class="main" id="nav">']
    for label,href,sub in NAV:
        is_active = (href==active) or (sub and active in SERVICE_PAGES and label=='Услуги')
        cls=' class="active"' if (is_active and not sub) else ''
        if sub:
            sub_active=' active' if active in SERVICE_PAGES else ''
            out.append('<div class="has-sub">')
            out.append(f'<a href="{href}" class="{("active" if sub_active else "").strip()}">{label} {ICON["chev"]}</a>')
            out.append('<div class="sub">')
            for sl,sh,si in sub:
                out.append(f'<a href="{sh}">{ICON[si]}{sl}</a>')
            out.append('</div></div>')
        else:
            out.append(f'<a href="{href}"{cls}>{label}</a>')
    out.append('</nav>')
    return '\n      '.join(out)

def head(title, desc, active):
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700;800&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/redesign.css">
</head>
<body>
<div class="topbar">
  <div class="wrap">
    <span class="l">{ICON['pin']} Транспортно-экспедиторская компания · Санкт-Петербург</span>
    <div class="r"><a href="mailto:info@mbm-trans.ru">info@mbm-trans.ru</a><a href="#" aria-label="Английская версия">EN</a></div>
  </div>
</div>
<header class="header" id="header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="МБМ-Транс — на главную">
      <img class="logo-img" src="assets/css/imgs/logo_h.jpg" srcset="assets/css/imgs/logo_h.jpg 1x, assets/css/imgs/logo_h@2x.jpg 2x" width="233" height="88" alt="МБМ-Транс">
    </a>
    {nav_html(active)}
    <div class="h-right">
      <div class="h-phone"><a href="tel:+78124016564">{ICON['phone']}+7 (812) 401-65-64</a><span>Звоните, мы на связи</span></div>
      <a href="kontaktyi.html" class="btn btn-orange">Заявка</a>
      <button class="burger" id="burger" aria-label="Открыть меню"><svg class="icon" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
    </div>
  </div>
</header>
<div class="overlay" id="overlay"></div>
'''

def page_hero(title, subtitle, crumb):
    cr=['<a href="index.html">Главная</a>']
    for label,href in crumb[:-1]:
        cr.append(f'<span class="sep">/</span><a href="{href}">{label}</a>')
    cr.append(f'<span class="sep">/</span><span aria-current="page">{crumb[-1][0]}</span>')
    return f'''<section class="page-hero">
  <div class="wrap">
    <nav class="breadcrumb" aria-label="Хлебные крошки">{''.join(cr)}</nav>
    <h1>{title}</h1>
    <p>{subtitle}</p>
  </div>
</section>'''

CTA = '''<hr class="hazard">
<div class="cta">
  <div class="wrap">
    <div><h2>Нужно перевезти негабаритный груз?</h2><p>Оставьте заявку — рассчитаем стоимость и сроки в течение рабочего дня.</p></div>
    <a href="kontaktyi.html" class="btn btn-orange">Оставить заявку %s</a>
  </div>
</div>''' % ICON['arrow']

def footer():
    return f'''<hr class="hazard">
<footer>
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <img class="foot-logo-img" src="assets/css/imgs/logo_f.png" srcset="assets/css/imgs/logo_f.png 1x, assets/css/imgs/logo_f@2x.png 2x" width="219" height="84" alt="МБМ-Транс">
      <p>Транспортно-экспедиторская компания. Перевозка негабаритных и тяжеловесных грузов собственным автопарком по всей России.</p>
    </div>
    <div class="foot-col"><h4>Услуги</h4>
      <a href="kontejnernyie-perevozki.html">Контейнерные перевозки</a>
      <a href="perevozka-negabaritnyix-gruzov.html">Негабаритные грузы</a>
      <a href="texnika-v-arendu.html">Техника в аренду</a>
      <a href="zhd-perevozki.html">Ж/Д перевозки</a>
    </div>
    <div class="foot-col"><h4>Компания</h4>
      <a href="o-kompanii.html">О компании</a>
      <a href="nashi-proektyi.html">Наши проекты</a>
      <a href="nashi-klientyi.html">Клиенты</a>
      <a href="kontaktyi.html">Контакты</a>
    </div>
    <div class="foot-col"><h4>Контакты</h4>
      <a href="tel:+78124016564">+7 (812) 401-65-64</a>
      <a href="mailto:info@mbm-trans.ru">info@mbm-trans.ru</a>
      <p>198035, Санкт-Петербург,<br>Межевой канал, д. 3, к. 2</p>
    </div>
  </div>
  <div class="wrap foot-bottom">
    <span>© 2008–2026 ООО «МБМ-Транс». Все права защищены.</span>
    <span>Перевозка негабаритных грузов · Санкт-Петербург</span>
  </div>
</footer>
<script>
const header=document.getElementById('header');
addEventListener('scroll',()=>header.classList.toggle('scrolled',scrollY>20),{{passive:true}});
const burger=document.getElementById('burger'),nav=document.getElementById('nav'),ov=document.getElementById('overlay');
function tm(){{const o=nav.classList.toggle('open');ov.classList.toggle('show',o);burger.setAttribute('aria-expanded',o)}}
burger.onclick=tm;ov.onclick=tm;
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
</script>
</body>
</html>'''

def write(fn, title, desc, active, hero, body):
    html = head(title,desc,active) + hero + '\n' + body + '\n' + CTA + '\n' + footer()
    open(fn,'w',encoding='utf-8').write(html)
    print('wrote',fn)

# ---------------- О КОМПАНИИ ----------------
about_body = f'''<section class="block">
  <div class="wrap content-grid">
    <article class="article prose reveal">
      <p><strong>ООО «МБМ-Транс»</strong> более 10 лет является одной из ведущих компаний Северо-Западного региона в области перевозок негабаритных и тяжеловесных грузов. Залогом успеха компании являются высокий профессионализм сотрудников и индивидуальный подход к каждому партнёру.</p>
      <p>Команда высококлассных и ответственных специалистов ежедневно обеспечивает качественное и своевременное предоставление услуг — ведь перевозка специализированных грузов это большая ответственность.</p>
      <h2>Полный цикл услуг</h2>
      <p>Компания специализируется на перевозке негабаритных и тяжеловесных грузов в любую точку России, стран СНГ, Балтии и Европы, оперируя собственным автопарком новейших автомобилей:</p>
      <ul>
        <li>25 автопоездов для перевозки негабаритных грузов массой <strong>до 200 тонн</strong></li>
        <li>Тягачи марок <strong>VOLVO, SCANIA, MERCEDES-BENZ</strong></li>
        <li>Полуприцепы <strong>NOOTEBOOM, GOLDHOFER, FAYMONVILLE</strong></li>
        <li>Более 30 собственных контейнерных площадок</li>
      </ul>
      <h2>Наша миссия</h2>
      <p>Стать лидером рынка перевозок негабаритных и тяжеловесных грузов, предоставляя клиентам безупречный сервис, надёжность и индивидуальный подход на всех этапах сотрудничества.</p>
      <p>Основные партнёры компании — крупнейшие российские предприятия: производители чёрных металлов, судостроительные, судоремонтные и машиностроительные предприятия, такие как ОАО «Северсталь», ФГУП «ПО «Севмаш», ООО «ОМЗ-Спецсталь» и другие.</p>
    </article>
    <aside class="sidebar">
      <div class="side-card reveal">
        <div class="person"><span class="av">МЮ</span><span><b>Мочалюк Юрий Борисович</b><small>Генеральный директор</small></span></div>
      </div>
      <div class="side-card accent reveal">
        <h4>Рассчитать перевозку</h4>
        <p>Опишите груз и маршрут — менеджер свяжется с вами в течение рабочего дня.</p>
        <a href="kontaktyi.html" class="btn btn-orange">Оставить заявку {ICON['arrow']}</a>
      </div>
    </aside>
  </div>
</section>
<hr class="hazard">
<div class="stats"><div class="wrap">
  <div class="stat reveal"><div class="ic">{ICON['truck']}</div><div class="num">25</div><div class="lbl">автопоездов в автопарке</div></div>
  <div class="stat reveal"><div class="ic">{ICON['box']}</div><div class="num">200<span class="u">т</span></div><div class="lbl">максимальный вес груза</div></div>
  <div class="stat reveal"><div class="ic">{ICON['doc']}</div><div class="num">30<span class="u">+</span></div><div class="lbl">контейнерных площадок</div></div>
  <div class="stat reveal"><div class="ic">{ICON['shield']}</div><div class="num">10<span class="u">+</span></div><div class="lbl">лет на рынке</div></div>
</div></div>'''
write('o-kompanii.html','О компании — МБМ-Транс',
      'ООО «МБМ-Транс» — более 10 лет на рынке перевозок негабаритных и тяжеловесных грузов. Собственный автопарк до 200 тонн.',
      'o-kompanii.html',
      page_hero('О компании','Более 10 лет надёжных перевозок негабаритных и тяжеловесных грузов собственным автопарком.',
                [('О компании','o-kompanii.html')]),
      about_body)

# ---------------- SERVICE PAGE BUILDER ----------------
def service(fn, title, subtitle, img, intro, h2, paras, bullets, persons):
    crumb=[('Услуги','kontejnernyie-perevozki.html'),(title,fn)]
    plist=''.join(f'<p>{p}</p>' for p in paras)
    blist='<ul>'+''.join(f'<li>{b}</li>' for b in bullets)+'</ul>' if bullets else ''
    pcards=''
    for nm,role,mail,initials in persons:
        mlink = '<a href="mailto:%s">%s</a>' % (mail,mail) if mail else ''
        pcards+=f'<div class="person"><span class="av">{initials}</span><span><b>{nm}</b><small>{role}</small>{mlink}</span></div>'
    side_persons=f'<div class="side-card reveal"><h4>Отдел</h4>{pcards}</div>' if persons else ''
    body=f'''<section class="block">
  <div class="wrap content-grid">
    <article class="article prose reveal">
      <img src="{img}" alt="{title}" style="width:100%;border-radius:var(--r);box-shadow:var(--shadow);margin-bottom:1.8rem">
      <p>{intro}</p>
      <h2>{h2}</h2>
      {plist}
      {blist}
    </article>
    <aside class="sidebar">
      {side_persons}
      <div class="side-card accent reveal">
        <h4>Нужен расчёт?</h4>
        <p>Оставьте заявку — рассчитаем стоимость и сроки.</p>
        <a href="kontaktyi.html" class="btn btn-orange">Оставить заявку {ICON['arrow']}</a>
      </div>
    </aside>
  </div>
</section>'''
    write(fn,f'{title} — МБМ-Транс',subtitle,fn,page_hero(title,subtitle,crumb),body)

service('kontejnernyie-perevozki.html','Контейнерные перевозки',
  'Автоперевозка всех типов морских контейнеров по России. Более 30 собственных контейнерных площадок.',
  'assets/images/fp_slider/slider2_.webp',
  'С 2005 года в список услуг компании «МБМ-Транс» включены контейнерные перевозки. Мы следим за тенденциями рынка и предлагаем клиентам только лучшие условия для сотрудничества.',
  'Особенности контейнерных перевозок',
  ['Контейнерные грузоперевозки позволяют решать ряд задач, связанных со снижением транспортных расходов и повышением рентабельности коммерческой деятельности. Мы используем автомобильный транспорт, что позволяет доставлять большие объёмы грузов в любую точку России — в том числе туда, где нет железнодорожного сообщения.'],
  ['Низкая себестоимость услуги — унифицированные размеры контейнеров упрощают погрузку и крепление','Груз защищён от дождя, ветра и хищений','Доставка непосредственно «до дверей» получателя','Универсальность — большинство грузов может перевозиться в контейнерах'],
  [('Пятаков Антон','Начальник отдела контейнерных перевозок','ap@mbm-trans.ru','ПА'),
   ('Завьялов Алексей','Менеджер отдела контейнерных перевозок','zas@mbm-trans.ru','ЗА')])

service('perevozka-negabaritnyix-gruzov.html','Перевозка негабаритных грузов',
  'Транспортировка крупногабаритных и тяжеловесных грузов массой до 200 тонн с полным сопровождением.',
  'assets/images/fp_slider/slider1_.webp',
  'Перевозка негабаритных грузов — ключевая специализация компании «МБМ-Транс». Мы располагаем собственным парком тягачей и низкорамных тралов, а также штатом опытных специалистов по проектной логистике.',
  'Что мы берём на себя',
  ['Груз считается негабаритным, если его ширина более 2,5 м, длина более 13,5 м, высота более 4 м, либо масса превышает 25 тонн. Перевозка таких грузов требует особой подготовки, разрешений и сопровождения.'],
  ['Разработка маршрута и схемы размещения груза','Оформление разрешений на перевозку негабарита','Автомобили сопровождения и взаимодействие с ГИБДД','Тягачи VOLVO, SCANIA, MERCEDES-BENZ и тралы до 200 тонн','Страхование груза на всю стоимость перевозки'],
  [])

service('texnika-v-arendu.html','Техника в аренду',
  'Специализированная техника для погрузки, разгрузки и транспортировки тяжёлых грузов.',
  'assets/images/crane.webp',
  'Компания «МБМ-Транс» предоставляет в аренду специализированную технику для проведения погрузочно-разгрузочных работ и транспортировки тяжёлых и негабаритных грузов.',
  'Доступная техника',
  ['Мы подберём технику под задачу любой сложности — от разовой погрузки до полного сопровождения проекта. Опытные операторы и техническое обслуживание включены.'],
  ['Автокраны грузоподъёмностью до 100 тонн','Низкорамные тралы и платформы','Тягачи для перевозки спецтехники','Сопровождение и услуги такелажа'],
  [])

service('zhd-perevozki.html','Ж/Д перевозки',
  'Перевозка грузов железнодорожным транспортом на универсальных и специальных платформах.',
  'assets/images/train.webp',
  'Для перевозок грузов железнодорожным транспортом компания «МБМ-Транс» оперирует универсальными платформами и организует мультимодальные схемы доставки.',
  'Преимущества Ж/Д перевозок',
  ['Железнодорожный транспорт оптимален для перевозки крупных партий грузов на дальние расстояния. Мы организуем доставку «от двери до двери», сочетая Ж/Д и автомобильное плечо.'],
  ['Универсальные и специальные платформы','Перевозка на дальние расстояния по выгодным тарифам','Мультимодальные схемы (Ж/Д + авто)','Полное экспедиторское сопровождение'],
  [])

# ---------------- ПРОЕКТЫ (все 28, hi-res webp) ----------------
import json
pmap=json.load(open('../original/projects_map.json',encoding='utf-8'))
def category(t):
    t=t.lower()
    if 'самолет' in t or 'вертолет' in t: return 'Авиатехника'
    if 'аэс' in t or 'гэс' in t or 'реактор' in t or 'турбин' in t or 'кондесатор' in t or 'ёмкости' in t or 'емкости' in t: return 'Энергетика'
    if 'контейнер' in t: return 'Контейнеры'
    if 'трамвай' in t or 'катер' in t or 'корабл' in t or 'трактор' in t or 'комбайн' in t or 'мойк' in t: return 'Спецтранспорт'
    if 'кран' in t or 'колесо' in t or 'свай' in t or 'установк' in t: return 'Спецтехника'
    if 'металлоконструкц' in t or 'конструкц' in t: return 'Металлоконструкции'
    return 'Оборудование'
cards=''
for base,title in pmap:
    tag=category(title)
    cards+=f'''<a class="proj reveal" href="#"><img src="assets/images/projects/{base}.webp" loading="lazy" alt="{title}"><div class="cap"><span class="tag">{tag}</span><b>{title}</b></div></a>'''
proj_body=f'''<section class="block"><div class="wrap"><div class="gallery">{cards}</div></div></section>'''
write('nashi-proektyi.html','Наши проекты — МБМ-Транс',
      'Реализованные проекты МБМ-Транс: перевозка самолётов, трамваев, оборудования для АЭС и другой техники.',
      'nashi-proektyi.html',
      page_hero('Наши проекты','От транспортировки трамваев и самолётов до оборудования для АЭС — реализованные перевозки любой сложности.',
                [('Наши проекты','nashi-proektyi.html')]),
      proj_body)

# ---------------- НОВОСТИ ----------------
news=[
 ('03','сен','Участие в строительстве объектов к ЧМ 2018','МБМ-Транс планирует принять участие в поставке строительных конструкций для возведения спортивных и инфраструктурных объектов к Чемпионату мира по футболу 2018 г.'),
 ('31','авг','Трасса Москва — Петербург превзойдёт немецкие автобаны','До ввода в эксплуатацию скоростной автомобильной дороги М-11 осталось менее 3 лет. По ряду параметров магистраль должна превзойти знаменитые немецкие автобаны.'),
 ('30','авг','МБМ-Транс доставляет конструкции для Керченского моста','С июля 2015 г. компания приступила к доставке мостовых конструкций для строительства временного моста через Керченский пролив.'),
 ('28','авг','Сбились с маршрута','Никита Музыря, общественный омбудсмен по защите прав предпринимателей в сфере транспорта, о наиболее эффективных механизмах защиты прав бизнеса.'),
]
items=''
for d,m,t,p in news:
    items+=f'''<a class="news-item reveal" href="#"><div class="date"><div class="d">{d}</div><div class="m">{m}</div></div><div><h3>{t}</h3><p>{p}</p></div></a>'''
news_body=f'''<section class="block"><div class="wrap"><div class="news-page-grid">{items}</div></div></section>'''
write('novosti.html','Новости — МБМ-Транс',
      'Новости компании МБМ-Транс.','novosti.html',
      page_hero('Новости','Будьте в курсе событий и проектов компании МБМ-Транс.',
                [('Новости','novosti.html')]),
      news_body)

# ---------------- КЛИЕНТЫ (все 20) ----------------
clients=[
 ('severstal-logo2','Северсталь'),('ижорский трубный завод','Ижорский трубный завод'),
 ('omz-logo','ОМЗ-Спецсталь'),('img2','Севмаш'),('logo_mostotrest','Мостотрест'),
 ('logo_inkotek','Инкотек'),('logo-nek','Группа компаний НЭК'),('logo_natrex','Natrex'),
 ('logo_bedford','Bedford Group'),('logo_instar','Instar Logistics'),
 ('logo_aettrans','AET Trans'),('ahlers_logo','Ahlers'),('logo_transy','Transport Systems Transy'),
 ('logo_premium_engineering','Premium Engineering'),('logo_lonmadi_kwintmadi','ЛОНМАДИ · КВИНТМАДИ'),
 ('logo_universal_spectech','Универсал Спецтехника'),('logo_ferronordic','Ferronordic Machines'),
 ('logo_keystone','Keystone Logistics'),('logo_asstra','AsstrA'),('logo_yusen','Yusen Logistics'),
]
cl=''
for base,alt in clients:
    cl+=f'<div class="client" title="{alt}"><img src="assets/images/clients/{base}.webp" loading="lazy" alt="{alt}"></div>'
clients_body=f'''<section class="block"><div class="wrap"><div class="client-page-grid">{cl}</div></div></section>'''
write('nashi-klientyi.html','Клиенты — МБМ-Транс',
      'Крупнейшие промышленные предприятия России — клиенты МБМ-Транс.','nashi-klientyi.html',
      page_hero('Наши клиенты','Крупнейшие промышленные предприятия России доверяют нам перевозку ответственных грузов.',
                [('Клиенты','nashi-klientyi.html')]),
      clients_body)

# ---------------- КОНТАКТЫ ----------------
contacts_body=f'''<section class="block">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-info reveal">
        <div class="row"><span class="ic">{ICON['pin']}</span><div><div class="lbl">Адрес</div><div class="val">Россия, 198035, Санкт-Петербург,<br>Межевой канал, д. 3, корпус 2, 8 этаж</div></div></div>
        <div class="row"><span class="ic">{ICON['phone']}</span><div><div class="lbl">Телефон</div><div class="val"><a href="tel:+78124016564">+7 (812) 401-65-64</a></div></div></div>
        <div class="row"><span class="ic">{ICON['mail']}</span><div><div class="lbl">E-mail</div><div class="val"><a href="mailto:info@mbm-trans.ru">info@mbm-trans.ru</a></div></div></div>
        <div class="row"><span class="ic">{ICON['clock']}</span><div><div class="lbl">Режим работы</div><div class="val">Пн–Пт 9:00–18:00 · сопровождение 24/7</div></div></div>
      </div>
      <form class="form reveal" onsubmit="return false">
        <h3>Оставить заявку</h3>
        <div class="fd">Заполните форму — менеджер свяжется с вами и рассчитает стоимость перевозки.</div>
        <div class="grid2">
          <div class="field"><label for="f-name">Контактное лицо</label><input id="f-name" type="text" placeholder="Ваше имя" required></div>
          <div class="field"><label for="f-phone">Телефон</label><input id="f-phone" type="tel" placeholder="+7 (___) ___-__-__" required></div>
        </div>
        <div class="field"><label for="f-email">E-mail</label><input id="f-email" type="email" placeholder="you@company.ru"></div>
        <div class="field"><label for="f-msg">Сообщение</label><textarea id="f-msg" placeholder="Опишите ваш груз и маршрут"></textarea></div>
        <button class="btn btn-orange" type="submit">Отправить заявку {ICON['arrow']}</button>
      </form>
    </div>
    <div class="maps">
      <div class="map"><span class="tab">{ICON['pin']}Офис</span><iframe loading="lazy" title="Офис" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d16001.552784463627!2d30.262006!3d59.912326!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469630be44f83dff%3A0x8c077b2fd2bd61ad!2sul.+Mezhevoy+kanal%2C+3%D0%BA2%2C+Sankt-Peterburg%2C+Russia%2C+198035!5e0!3m2!1sen!2s!4v1417777839462"></iframe></div>
      <div class="map"><span class="tab">{ICON['pin']}База</span><iframe loading="lazy" title="База" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d16091.96295086256!2d30.068682!3d59.724583!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469617d23744dca9%3A0xb7c01e57da5b5d7b!2sKingiseppskoye+sh.%2C+47%2C+Krasnoye+Selo%2C+g.+Sankt-Peterburg%2C+Russia%2C+198320!5e0!3m2!1sen!2s!4v1417777919444"></iframe></div>
    </div>
  </div>
</section>'''
write('kontaktyi.html','Контакты — МБМ-Транс',
      'Контакты ООО «МБМ-Транс»: Санкт-Петербург, Межевой канал, д.3. Телефон +7 (812) 401-65-64.',
      'kontaktyi.html',
      page_hero('Контакты','Свяжитесь с нами удобным способом — мы на связи в рабочее время и сопровождаем перевозки 24/7.',
                [('Контакты','kontaktyi.html')]),
      contacts_body)

print('\nAll inner pages generated.')
