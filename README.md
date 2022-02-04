<h1>job-interview-test-tasks</h1>
<p align="justify">This is a realization of several tasks for getting a job in a company "Soft project"</p>

<h1>Краткие сведения о репозитории</h1>
<p align="jusify">В этой главе пойдут сведения для моего дневника, поэтому, дорогой читатель, если вам это неинтересно, и вы хотите сразу перейти к делу, то открывайте <a href="#main">следующую главу</a>!)</p>

<p align="jusify">Этот репозиторий я залил днём 4-го февраля 22-го года. Перед этим в течение пяти дней я выполнял задания от компании <b>"Софт Проект"</b>, чтобы ребята из этой компании обратили на меня своё внимание и пригласили к себе на собеседование.</p>

<p align="jusify">28-го числа января я зашёл на <b>"hh.ru"</b> из-за небходимости найти какой-то заработок и присоединиться к классной команде разработчиков, чтобы вместе помогать людям в сфере IT. Подал заявки на несколько вакансий в хорошие компании, это были: <i>"ЛАНИТ — Би Пи Эм"</i> (на стажировку для обучения программированию в области BPM — BUSINESS PROCESS MANAGEMENT), <i>"Bip.ru"</i> на Андроид-программиста, сам <i><b>"Софт Проект"</b></i>, тоже на хорошую стажировку с удобными для меня условиями работы после неё (она длится шесть месяцев и на ней изучают <b>Ruby</b>), и в несколько других компаний. В этот же день мне ответили сразу две компании, и одна из них — "Софт Проект". Я заполнил анкету о себе и 29-го числа начал выполнять тестовые задания, завершил которые 3 февраля (то есть вчера на момент написания этой статьи).</p>

<p align="jusify">Одно, последнее по списку, задание я не успел выполнить, но остальные успешно сделал. И некоторые из этих заданий я покажу в этом репозитории вам, читатель, чтобы вы были в курсе этого!</p>

<h1 name="main">Описание заданий и их возможных решений</h1>
<h2>Введение</h2>
<p align="jusify">Суть большинства заданий заключается в том, чтобы, прочитав условие, считать с помощью любого на Ваш выбор языка программирования исходный файл к соответствующему заданию и обработать его с целью достижения решения задачи.</p>

<p align="jusify">Реализация задач в этом репозитории представлена исключительно в виде Python-кода. Всего заданий было десять штук — здесь будет часть из них. Но этого вполне достаточно для вашего понимания, что вас будет ждать на собеседованиях на похожие вакансии!</p>

<p align="jusify">Если вы не очень сильны в программировании именно на Python, то предлагаю вам посетить metanit: https://metanit.com/python/tutorial/. Здесь очень доступно объяснено ООП в Питоне, его основные конструкции (циклы и условия), порядок обработки исключений (try...except), работа с файлами и даже создание простых графических приложений с помощью встроенного в Python модуля — Tkinter. В общем на этом сайте есть всё самое основное для умения прекрасно и эллегантно создавать код на Python! Конечно, пользуйтесь ещё и своими любимыми источниками, читатель — я только предложил!</p>

<p align="jusify">Если Вы хотите программировать на другом языке, скажем, C#/C++, Java или Pascal, то флаг Вам в руки!) Самое главное, чтобы вам было интересно выполнять задания, и вы видели в этом смысл для себя!</p>

<p align="jusify"></p>

<h2>Цель работы</h2>
<p align="jusify">Выполняя эти задания на каком-либо языке программирования, вы отлично натренируете свои навыки в обработке файлов, в построении циклов и во многих других мелочах. Кроме того, вы наберётесь полезного опыта разработки небольших специализированных утилит.</p>

<h2>Список заданий</h2>
<p align="jusify">Условия задач я изложу вам примерно, на память, самое главное:
<ol>
  <li>
    <p align="jusify">У некоторой компании есть своя сеть и список ip-адресов компьютеров в ней. IP-адреса перечислены в файле <code><a href="1.txt">1.txt</a></code> (см. файлы этого репозитория). Это образный, придуманный формат ip-адресов (составитель задачи назвал их IPv7).</p>
    <p align="jusify">Из структуры этих адресов можно однозначно понять, поддерживает ли соответствующий компьютер с данным ip, некоторую сетевую технологию.</p>
    <p align="jusify">Вам необходимо выяснить, какие узлы сети поддерживают эту технологию. Правила такие:
    <ul>
      <li>
        <p align="jusify">Пусть IP-адреса состоят только из букв латинского алфавита и будут произвольной длины, причём каждый адрес поделён на части: квадратные скобки (одна или несколько пар) также вставлены в адреса. Например, ip может выглядить так:<br></p>
        <p name="first" align="center">1) <code>aba[bab]</code></p>
        <p name="second" align="center">2) <code>adakh[babd]pp</code></p>
        <p name="third" align="center">3) <code>grkrh[bkooi]pp[krk]</code></p>
      </li>
      <li>
        <p align="jusify">Известно, что узел с соответствующим ip-адресом поддерживает обсуждаемую сетевую технологию, если его адрес имеет вне квадратных скобок последовательность <b>"ABA"</b>, которой соответствует последовательность в квадратных скобках <b>"BAB"</b>. Это последовательности из трёх символов, первая из которых — ABA — заканчивается двумя одинаковыми буквами, равными букве в середине последовательности BAB; и ABA имеет в середине букву, которой заканчивается последовательность в квадртаных скобках BAB. Если в адресе в квадратных скобках есть последовательность BAB и соответствующая ей последовательность вне квадратных скобок ABA, не важно в каких количествах, — то этот адрес поддерживает сетевую технологию.</p>
        <p align="jusify">К примеру, такую технологию поддерживают компьютеры с первым адресом (см. <a href="#first">выше</a>) и с <a name="#third">третьим</a>; и не поддерживает второй компьютер со <a name="#second">вторым</a> ip-шником.</p>
      </li>
    </ul>
    </p>
  </li>
</ol>
</p>
