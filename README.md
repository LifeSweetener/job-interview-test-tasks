<h1>job-interview-test-tasks</h1>
<p align="justify">This is a realization of several tasks for getting a job in a company "Soft project"</p>

<h1>Краткие сведения о репозитории</h1>
<p align="jusify">В этой главе пойдут сведения для моего дневника, поэтому, дорогой читатель, если вам это неинтересно, и вы хотите сразу перейти к делу, то открывайте <a href="#main">следующую главу</a>!)</p>

<p align="jusify">Этот репозиторий я залил днём 4-го февраля 22-го года. Перед этим в течение пяти дней я выполнял задания от компании <b>"Софт Проект"</b> (см. http://soft-project.ru/), чтобы ребята из этой компании обратили на меня своё внимание и пригласили к себе на собеседование.</p>

<p align="jusify">28-го числа января я зашёл на <b>"hh.ru"</b> из-за небходимости найти какой-то заработок и присоединиться к классной команде разработчиков, чтобы вместе помогать людям в сфере IT. Подал заявки на несколько вакансий в хорошие компании, это были: <i>"ЛАНИТ — Би Пи Эм"</i> (на стажировку для обучения программированию в области BPM — BUSINESS PROCESS MANAGEMENT), <i>"Bip.ru"</i> на Андроид-программиста, сам <i><b>"Софт Проект"</b></i>, тоже на хорошую стажировку с удобными для меня условиями работы после неё (она длится шесть месяцев и на ней изучают <b>Ruby</b>), и в несколько других компаний. В этот же день мне ответили сразу две компании, и одна из них — "Софт Проект". Я заполнил анкету о себе и 29-го числа начал выполнять тестовые задания, завершил которые 3 февраля (то есть вчера на момент написания этой статьи).</p>

<p align="jusify">Одно, последнее по списку, задание я не успел выполнить, но остальные успешно сделал. И некоторые из этих заданий я покажу в этом репозитории вам, читатель, чтобы вы были в курсе этого!</p>

<h1 name="main">Описание заданий и их возможных решений</h1>
<h2>Содержание</h2>
  <p align="jusify">
    <ul>
      <li><a href="#intro">Введение</a></li>
      <li><a href="#goal">Цель работы</a></li>
      <li><a href="#list">Список заданий</a>
        <ol type="1">
          <li><a href="#task1">Сеть компании</a></li>
          <li><a href="#task2">Электрическая схема</a></li>
          <li><a href="#task3">Охрана раздевалки</a></li>
          <li><a href="#pswd">Расшифровка пароля</a></li>
          <li><a href="#5 task">Сломанный экран</a></li>
        </ol>
      </li>
      <li><a href="#comments">Комментарии к коду в репозитории</a>
        <ol type="1">
          <li><a href="#code1">Сеть компании</a></li>
          <li><a href="#code2">Электрическая схема</a></li>
          <li><a href="#code3">Охрана раздевалки</a></li>
          <li><a href="#code4">Расшифровка пароля</a></li>
          <li><a href="#code5">Сломанный экран</a></li>
        </ol>
      </li>
      <li><a href="#ans">Ответы к заданиям</a></li>
    </ul>
  </p>
<h2 name="intro">Введение</h2>
<p align="jusify">Суть большинства заданий заключается в том, чтобы, прочитав условие, считать с помощью любого на Ваш выбор языка программирования исходный файл к соответствующему заданию и обработать его с целью достижения решения задачи.</p>

<p align="jusify">Реализация задач в этом репозитории представлена исключительно в виде Python-кода. Всего заданий было десять штук — здесь будет часть из них. Но этого вполне достаточно для вашего понимания, что вас будет ждать на собеседованиях на похожие вакансии!</p>

<p align="jusify">Если вы не очень сильны в программировании именно на Python, то предлагаю вам посетить metanit: https://metanit.com/python/tutorial/. Здесь очень доступно объяснено ООП в Питоне, его основные конструкции (циклы и условия), порядок обработки исключений (try...except), работа с файлами и даже создание простых графических приложений с помощью встроенного в Python модуля — Tkinter. В общем на этом сайте есть всё самое основное для умения прекрасно и эллегантно создавать код на Python! Конечно, пользуйтесь ещё и своими любимыми источниками, читатель — я только предложил!</p>

<p align="jusify">Если Вы хотите программировать на другом языке, скажем, C#/C++, Java или Pascal, то флаг Вам в руки!) Самое главное, чтобы вам было интересно выполнять задания, и вы видели в этом смысл для себя!</p>

<p align="jusify"></p>

<h2 name="goal">Цель работы</h2>
<p align="jusify">Выполняя эти задания на каком-либо языке программирования, вы отлично натренируете свои навыки в обработке файлов, в построении циклов и во многих других мелочах. Кроме того, вы наберётесь полезного опыта разработки небольших специализированных утилит.</p>

<h2 name="list">Список заданий</h2>
<p align="jusify">Условия задач я изложу Вам примерно, на память, иногда что-то буду добавлять от себя (<a href="#5 task">пятую задачу</a> в этом списке я дословно скопировал):
<ol>
  <li>
    <h3 name="task1">Сеть компании</h3>
    <p align="jusify">У некоторой компании есть своя сеть и список ip-адресов компьютеров в ней. IP-адреса перечислены в файле <code><a href="1.txt">1.txt</a></code> (см. файлы этого репозитория). Это образный, придуманный формат ip-адресов (составитель задачи назвал их IPv7).</p>
    <p align="jusify">Из структуры этих адресов можно однозначно понять, поддерживает ли соответствующий компьютер с данным ip, некоторую сетевую технологию.</p>
    <p align="jusify">Вам необходимо выяснить, какие узлы сети поддерживают эту технологию. Правила такие:
    <ul>
      <li>
        <p align="jusify">Пусть IP-адреса состоят только из букв латинского алфавита и будут произвольной длины, причём каждый адрес поделён на части: квадратные скобки (одна или несколько пар) также вставлены в адреса. Например, ip может выглядить так:<br></p>
        <table align="center"><tr><td>
        <p align="center">1) <code>aba[bab]</code></p>
        <p align="center">2) <code>adakh[babd]pp</code></p>
        <p align="center">3) <code>grkrh[bkooi]asz[krk]</code></p>
        <p name="example1" align="center"><b>ПРИМЕР 1</b></p>
      </td></tr></table>
      </li>
      <li>
        <p align="jusify">Известно, что узел с соответствующим ip-адресом поддерживает обсуждаемую сетевую технологию, если его адрес имеет вне квадратных скобок последовательность <b>"ABA"</b>, которой соответствует последовательность в квадратных скобках <b>"BAB"</b>. Это последовательности из трёх символов, первая из которых — ABA — заканчивается двумя одинаковыми буквами, равными букве в середине последовательности BAB; и ABA имеет в середине букву, которой заканчивается последовательность в квадртаных скобках BAB. Если в адресе в квадратных скобках есть последовательность BAB и соответствующая ей последовательность вне квадратных скобок ABA, не важно в каких количествах, — то этот адрес поддерживает сетевую технологию.</p>
        <p align="jusify">К примеру, такую технологию поддерживают компьютеры с первым адресом (см. <a href="#example1">пример выше</a>) и с третьим — <code>g<b>RKR</b>h[bkooi]asz[<b>KRK</b>]</code>; и не поддерживает второй компьютер со вторым ip-шником.</p>
      </li>
    </ul>
    </p>
  </li>
  
  <li>
  <h3 name="task2">Электрическая схема</h3>
  <p align="jusify">Это задание связано с проводами и логическими вентилями. Представьте, что Вам дали совокупность проводов и набор логических вентилей, к которым подсоединяются эти провода: вентиль "NOT", вентиль "AND", "OR", "LSHIFT" и "RSHIFT" — всего пять разновидностей логических вентилей. Вам сказали собрать логическую схему из этого набора проводов и вентилей с помощью инструкции (см. файл этого репозитория <code><a href="2.txt">2.txt</a></code>).</p>
  <p align="jusify">Каждый провод может иметь в себе сигнал (выражающийся любым числом по модулю в пределах от 0 до 65535). Логические вентили могут иметь один или два входа и имеют один выход — они не заработают и не подадут на выход сигнал, если на каком-либо из их входов не будет сигнала. Знак выхода вентиля и, значит, входа провода обозначается как <code>-></code>.</p>
    <p align="jusify">Например, пусть у нас в наличии будет пять проводов: <code>a</code>, <code>b</code>, <code>c</code>, <code>d</code> и <code>e</code>. Тогда следующая инструкция:<br></p>
  <table align="center"><tr><td>
    <ol type="1">
      <li><p align="center"><code>1 -> a</code></p></li>
  <li><p align="center"><code>5 -> b</code></p></li>
  <li><p align="center"><code>NOT a -> c</code></p></li>
  <li><p align="center"><code>e OR b -> d</code></p></li>
  <li><p align="center"><code>c LSHIFT b -> e</code></p></li>
    </ol>
    <p name="example2" align="center"><b>ПРИМЕР 2</b></p>
    </td></tr></table>
  <p align="jusify">при первом проходе подаст сигнал на такие провода: <code>a = 1</code>, <code>b = 5</code>, <code>c = -2</code> и <code>e = -64</code>. Но провод <code>d</code> будет без сигнала, потому что при подходе к нему сигнал провода <code>e</code> отсутствовал (см. четвёртую строку в <a href="#example2">примере</a>), и вентиль "OR" не заработал.</p>
  <p align="jusify">Это значит, что нужно сделать ещё один проход по инструкции с уже известными сигналами проводов. Тогда сигнал в проводе <code>d</code> появится и станет равным значению <code>-59</code>!</p>
  <p align="jusify">1. Каким будет значение провода <code>a</code> по вашей инструкции?</p>
  <p align="jusify">2. Если у вас получилось выявить значение сигнала провода <code>a</code>, то начните собирать схему заново по той же инструкции; но только проводу <code>b</code> вместо значения, указанного в этой инструкции, подайте другое значение — значение провода <code>a</code>, полученное в первом пункте задачи. А теперь какой сигнал у Вас получился на проводе <code>a</code>?
</li>

<li>
  <h3 name="task3">Охрана раздевалки</h3>
  <p align="jusify">Вам с вашими друзьями нужно пройти через охрану одной раздевалки, чтобы украсть футболку известнейшего спортсмена. Вы по очереди записываете в журнал время дежурства всех охранников и подмечаете, когда они засыпают и просыпаются. Получилась такая сводка — <a href="3.txt">3.txt</a>.</p>
  <p align="jusify">Вы вместе с друзьями также замечаете, что охранники всегда засыпают между полуночью и часом ночи. Поэтому остаются важны только сами минуты, а не часы!</p>
  <p align="jusify">Например, ниже показан журнал с двумя охранниками, сменяющими друг друга.</p>
  <table align="center"><tr><td>
  <p align="center"><code>[2022-01-01 23:54] Guard #123 begins shift</code><br></p>
  <p align="center"><code>[2022-01-01 00:11] falls asleep</code><br></p>
  <p align="center"><code>[2022-01-01 00:34] wakes up</code><br></p>
  <p align="center"><code>[2022-01-01 00:39] Guard #654 begins shift</code><br></p>
  <p align="center"><code>[2022-01-01 00:50] falls asleep</code><br></p>
  <p align="center"><code>[2022-01-01 00:58] wakes up</code><br></p>
  <p align="center"><code>[2022-01-02 23:59] Guard #654 begins shift</code><br></p>
  <p align="center"><code>[2022-01-02 00:06] falls asleep</code><br></p>
  <p align="center"><code>[2022-01-02 00:20] wakes up</code><br></p>
  <p align="center"><code>[2022-01-02 00:25] Guard #123 begins shift</code><br></p>
  <p align="center"><code>[2022-01-02 00:33] falls asleep</code><br></p>
  <p align="center"><code>[2022-01-02 00:50] wakes up</code><br></p>
  <p name="example3" align="center"><b>ПРИМЕР 3</b></p>
  </td></tr></table>
  <p align="jusify">Можно построить таблицу, чтобы было нагляднее, и Вам было ясно, о чём речь:</p>
  <p align="justify">
    <table align="center">
      <tr>
      <td><b>День дежурства</b></td><td><b>Номер охранника</b></td><td colspan="60"><b>Минуты</b></td>
      </tr>
      <tr>
        <td></td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>28</td><td>29</td><td>30</td><td>31</td><td>32</td><td>33</td><td>34</td><td>35</td><td>36</td><td>37</td><td>38</td><td>39</td><td>40</td><td>41</td><td>42</td><td>43</td><td>44</td><td>45</td><td>46</td><td>47</td><td>48</td><td>49</td><td>50</td><td>51</td><td>52</td><td>53</td><td>54</td><td>55</td><td>56</td><td>57</td><td>58</td><td>59</td><td>60</td>
      </tr>
      <tr>
        <td>01.01.2022</td><td>#123</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td>
      </tr>
      <tr>
        <td>01.01.2022</td><td>#654</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>.</td><td>.</td><td>.</td>
      </tr>
      <tr>
        <td>01.02.2022</td><td>#654</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td<td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td>
      </tr>
      <tr>
        <td>01.02.2022</td><td>#123</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>#</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td>
      </tr>
    </table>
  </p>
  <p align="jusify">В таблице точками отмечено время бодрствования охраны, а символами решётки (<code>#</code>) показано время сна охранников.</p>
  <p align="jusify">Обратите внимание, что охранники считаются спящими уже в момент начала их сна: <code>falls asleep</code> в журнале; тогда как они считаются бодрствующими, начиная непосредственно со времени, когда они просыпаются: <code>wakes up</code> в журнале.
  <p align="jusify">Определите по своим записям номер охранника, который чаще других спал в конкретную минуту, и саму эту минуту, когда этот охранник спал чаще, чем все остальные охранники в любую другую минуту. Ответ дайте в виде произведения номера охранника на соответствующую минуту.</p>
  <p align="jusify">Так, в <a href="#example3">примере 3</a> из таблицы наглядно видно, что охранник под номером <code>#123</code> дважды подряд спал в <code>33</code>-ью минуту. Но в остальное время оба охранника спали в совершенно разные моменты времени. Значит, ответ в этом случае будет такой:</p>
  <p align="center"><br><code>123 x 33 = <b>4059</b></code><br></p>
</li>

<li>
  <h3 name=pswd>Расшифровка пароля</h3>
  <p align="jusify">В четвёртой задаче Вам необходимо разгадать восьмисимвольный пароль от двери. Дверь имеет свой идентификатор, к примеру <code>asd</code>; кроме того, Вам известно, что для расшифровки пароля от двери понадобится ещё и целочисленный индекс значением от нуля и до бесконечности. Идентификатор (id) и индекс сливаются друг с другом в одну строку, и уже от неё вычисляется хеш-функция — <code>md5</code>. Если получившийся от этой функции хеш начинается с пяти нулей, то эта комбинация id и числового индекса подобрана правильно.</p>
  <p align="jusify">Из этого корректного хеша требуется взять шестой по счёту символ, который укажет на позицию символа в пароле, а сам символ нужно взять с седьмого по порядку места в получившемся хеше. Причём, если позиция в пароле, на которую указывает шестой символ правильного хеша, уже занята найденным ранее символом или выходит за границы длины пароля, то необходимо продолжить алгоритм подбора пароля, пропустив этот хеш.</p>
  <p align="jusify">Идентификатор от Вашей двери — <code>fkylfhsq</code>.</p>
</li>

<li>
  <h3 name="5 task">Сломанный экран</h3>
  <p align="jusify">Вы натыкаетесь на дверь, за которой реализуется то, что, как вы можете предположить, является реализацией двухфакторной аутентификации.</p>

<p align="jusify">Чтобы пройти через дверь, сначала нужно провести по ней карточкой-ключом (это не проблема, она лежала на соседнем столе). Затем на маленьком экране появляется код, который вы вводите на клавиатуре. Затем, предположительно, дверь отпирается.</p>

<p align="jusify">К сожалению, экран был разбит. Через несколько минут вы все разобрали и поняли, как все работает. Теперь вам осталось выяснить, что должно было отображаться на экране.</p>

<p align="jusify">Магнитная полоса на карточке, которую вы провели, кодирует серию инструкций для экрана; эти инструкции доступны в файле <code><a href="5.txt">5.txt</a></code>. Экран имеет ширину 50 пикселей и высоту 6 пикселей, и способен выполнять три несколько своеобразные операции:<br></p>
<table align="center"><tr><td>
  <p align="center"><code><b>rect AхB</b> включает все пиксели в прямоугольнике в верхнем левом углу экрана, который имеет ширину A и высоту B.</code></p>

  <p align="center"><code><b>rotate row y=A by B</b> сдвигает все пиксели в строке A (0 — верхняя строка) вправо на B пикселей. Пиксели, которые упадут за правый край, появятся в левом конце строки.</code></p>

  <p align="center"><code><b>rotate column x=A by B</b> сдвигает все пиксели в столбце A (0 — левый столбец) вниз на B пикселей. Пиксели, которые упадут снизу, появятся вверху столбца.</code></p>
</td></tr></table>
  
  <p align="jusify">Например, вот простая последовательность на меньшем экране:<br></p>

  <p align="center"><code>- rect 3х2 создает небольшой прямоугольник в верхнем левом углу:</code><br></p>
  <table align="center">
    <tr>
      <td>#</td><td>#</td><td>#</td><td>.</td><td>.</td><td>.</td>
    </tr>
    <tr>
      <td>#</td><td>#</td><td>#</td><td>.</td><td>.</td><td>.</td>
    </tr>
    <tr>
      <td>.</td><td>.</td><td>.</td><td>.</td><td>.</td><td>.</td>
    </tr>
  </table>
<p align="center"><code>- rotate column x=1 by 1 поворачивает второй столбец вниз на один пиксель:</code><br></p>
  <table align="center">
    <tr>
      <td>#</td><td>.</td><td>#</td><td>.</td><td>.</td><td>.</td>
    </tr>
    <tr>
      <td>#</td><td>#</td><td>#</td><td>.</td><td>.</td><td>.</td>
    </tr>
    <tr>
      <td>.</td><td>#</td><td>.</td><td>.</td><td>.</td><td>.</td>
    </tr>
  </table>
<p align="center"><code>- rotate row y=0 by 4 поворачивает верхнюю строку вправо на четыре пикселя:</code><br></p>

  <table align="center">
    <tr>
      <td>#</td><td>.</td><td>.</td><td>.</td><td>#</td><td>.</td>
    </tr>
    <tr>
      <td>#</td><td>#</td><td>#</td><td>.</td><td>.</td><td>.</td>
    </tr>
    <tr>
      <td>.</td><td>#</td><td>.</td><td>.</td><td>.</td><td>.</td>
    </tr>
  </table>
<p align="center"><code>- rotate column х=1 by 1 снова поворачивает второй столбец на один пиксель вниз, в результате чего нижний пиксель возвращается к вершине:</code><br></p>

  <table align="center">
    <tr>
      <td>#</td><td>#</td><td>.</td><td>.</td><td>#</td><td>.</td>
    </tr>
    <tr>
      <td>#</td><td>.</td><td>#</td><td>.</td><td>.</td><td>.</td>
    </tr>
    <tr>
      <td>.</td><td>#</td><td>.</td><td>.</td><td>.</td><td>.</td>
    </tr>
  </table>
<p align="jusify">Вы замечаете, что экран способен отображать только заглавные буквы; в используемом шрифте каждая буква имеет ширину 5 пикселей и высоту 6 пикселей.</p>

<p align="jusify">Какой код пытается отобразить экран после того, как вы проводите картой (инструкции в файле <code><a href="5.txt">5.txt</a></code>)?</p>
</li>
</ol>
</p>

<h2 name="comments">Комментарии к коду в репозитории</h2>
<h3 name="code1">Сеть компании</h3>
<p align="jusify">Эта задача проверяет Ваше умение с помощью любого языка программирования (ЯП) обрабатывать строки. В Python для этого есть специальный встроенный модуль для работы со строками. <i>Строка</i> в Python — это неизменяемый тип данных. То есть любая Python-функция, изменяющая строки, не изменяет строку напрямую, а создаёт её копию строго определённым образом, как того требует задача, ею решаемая.</p>

<p align="jusify">В этом задании не нужно изменять строки, содержащие ip-адреса узлов сети компании. Вместо этого их нужно просто прочитать и найти определённое совпадение между троицами символов вне квадратных скобок и троицами, заключённых в эти скобки, каждого ip-адреса.</p>

<p align="jusify">По итогу, в процессе выполнения кода создаются две строки: <code>troika_aba</code> и <code>troika_bab</code>, которые и содержат все возможные троицы символов из адресов и которые и сравниваются. Ключевое условие в коде <code><a href="1.py">1.py</a></code>, это:<br></p>

<table align="center"><tr><td>
  <p align="center"><code><...></code></p>
  <p align="center"><code><i>46. </i><b>if</b> (troika_aba[0] == troika_bab[1]) <b>and</b> (troika_aba[2] == troika_bab[1]) <b>and</b> (troika_aba[1] == troika_bab[0]) <b>and</b> (troika_aba[1] == troika_bab[2]):</code></p>
  <p align="center"><code><...></code></p>
</td></tr></table>
  
<p align="jusify">Здесь сравниваются крайние символы одной строки с серединным символом другой и наоборот.</p>

<p align="jusify">Также можно дать описание первым трём строкам кода <code><a href="1.py">1.py</a></code>:</p>

<table align="center"><tr><td>
  <p align="center"><code><i>1. </i><b># Подготовить исходные данные для обработки:</b></code></p>
  <p align="center"><code><i>2. </i>file = open("C:\\Users\\User_ll\\Downloads\\07.txt")</code></p>
  <p align="center"><code><i>3. </i><b>data</b> = file.readlines()</code></p>
  <p align="center"><code><i>4. </i>file.close()</code></p>
  <p align="center"><code><...></code></p>
</td></tr></table>

<p align="jusify">После выполнения этих функций и операторов в переменную <code>data</code> попадает <i>Python-список</i>, элементами которого являются ip-адреса — строки. И который в следующем <code>for</code>-цикле программа поочерёдно обрабатывает, определяя подходящие ip-шники и суммируя их кол-во в переменной <code>counter</code>.</p>

<h3 name="code2">Электрическая схема</h3>
<p align="jusify">Это задание оттачивает Ваш навык владения поразрядной арифметикой в каком-либо, подходящим для Вас ЯП. Здесь отрабатывается знание таких поразрядных операций, как: НЕ, И, ИЛИ, СДВИГ ВПРАВО и СДВИГ ВЛЕВО.</p>

<p align="jusify">В Python они представлены соответсвующими битовыми операторами (см. про них подробнее тут: https://www.bestprog.net/ru/2019/10/21/python-bitwise-operators-ru/):
  <ul>
    <li><code>~</code> — битовый оператор <b>"НЕТ"</b>;</li>
    <li><code>&</code> — битовый оператор <b>"И"</b>;</li>
    <li><code>|</code> — битовый оператор <b>"ИЛИ"</b>;</li>
    <li><code>&gt;&gt;</code> — битовый оператор <b>"СДВИГ ВПРАВО"</b>;</li>
    <li><code>&lt;&lt;</code> — битовый оператор <b>"СДВИГ ВЛЕВО"</b>.</li>
  </ul>
</p>

<p align="jusify">Смысл кода не так сложен, как казалось бы — в цикле, до тех пор пока не будут определены сигналы у всех проводов выполнять заданные в файле <code><a href="2.txt">2.txt</a></code> инструкции. Каждому программисту известно, что всегда трудновато читать и вникать в чужой код, нежели чем в свой. Поэтому не бойтесь, как выглядит код к этому заданию: <code><a href="2.py">2.py</a></code>.</p>

<p align="jusify"><code>vars</code> — это <i>Python-словарь</i>, который в качестве ключей хранит в себе названия проводов, а в качестве значений — значения их сигналов. (В коде он уже инициализирован: это значения, которые получились в процессе отладки и тестирования — его можно спокойно, если Вам это интересно, инициализировать как пустой словарь).</p>

<p align="jusify">Переменная <code>sos</code> хранит логические <code>True</code> или <code>False</code> и является признаком (в программировании обычно такие переменные называют <i>флагом</i>) того, что какой-то провод в процессе выполнения инструкции <code><a href="2.txt">2.txt</a></code> не получил свой сигнал. Другими словами, <code>sos = True</code> означает, что главный цикл исполнения инструкции (<code><b>while</b> (sos):</code>) нужно ещё раз повторить в будущем.</p>

<p align="jusify">В цикле <code><b>for</b> line <b>in</b> data:</code> обрабатывается каждая строка инструкции: она разбивается по операндам (переменные <code>var1</code> и <code>var2</code>), определяется операция в ней (переменная <code>action</code>) и результирующий провод (переменная <code>result</code>). Затем эта операция вычисляется и результат сохраняется в словарь <code>vars</code> под соответствующим ключом.</p>

<h3 name="code3">Охрана раздевалки</h3>
<p align="jusify">Здесь также, как и в предыдущем задании, применяется Python-словарь для составления условной таблицы с пометками о времени сна и бодрствования всех охранников, указанных в исходных данных: <code><a href="3.txt">3.txt</a></code>.</p>

<p align="jusify">Важным моментом в реализации этой задачи для более удобного и быстрого её решения становится сортировка исходных данных:<br></p>
<p align="center"><code>data.<b>sort</b>(<b>key</b> = lambda x: x[2:18])</code></p>
<p align="jusify">У функции сортировки <code>sort()</code> в Python есть параметр <code>key</code>, который задаёт порядок сортировки любого итерируемого объекта: списка, строки, словаря или кортежа. В коде в данном случае сказано интерпретатору Python сортировать записи об охране, учитывая только дату, указанную в квадратных скобках (см. файл <code><a href="3.txt">3.txt</a></code>). <code>lambda</code> означает создание простой <i>анонимной функции</i> (<i>лямбда-функции</i>), которая передаётся в параметр <code>key</code>.</p>

<h3 name="code4">Расшифровка пароля</h3>
<p align="jusify">Здесь стоит отметить, что в Python есть библиотека <code>hashlib</code>, которая включает в себя функцию <code>md5()</code>. Она становится центральной в этом коде, потому что представляет собой хеш-функцию, через которую нужно прогонять id двери и целочисленный индекс, начиная с нуля (см. <a href="#pswd">Условие этого задания</a> выше).</p>

<h3 name="code5">Сломанный экран</h3>
<p align="jusify">В этом задании задействованы Python-средства ООП для разнообразия. В коде <code><a href="5.py">5.py</a></code> присутствуют два <i>класса</i>: <code>Screen</code>, представляющий экран и реализацию три его основных алгоритма (<code>rect</code>, <code>rotate row</code> и <code>rotate column</code> — см. <a href="#5 task">Условие этого задания</a>), и <code>Main</code>, с помощью которого запускается на выполнение обсуждаемый скрипт.</p>

<p align="jusify">Класс — это внутреннее строение (или шаблон) любого объекта, представляющего этот класс. В классе задаются все функции (методы) и переменные (состояния) будущих объектов этоо класса. А объекты просто воплощают свой класс в процессе работы программы. К примеру, люди имеют ноги, руки и голову, могут бегать, говорить и целоваться; то есть люди — это класс. А Петя и Диана — это воплощения этого класса: они люди, но каждый со своими уникальными ногами, руками и головой и способностями. К примеру, в <code><a href="5.py">5.py</a></code> <code>Screen</code> — класс, а <code>screen</code> — объект:<br></p>

<p align="center"><code><i>93:</i> screen = Screen()</code></p>

<p align="jusify">Функция <code>__init__(self)</code> (но в случае ООП принято называть её <i>методом</i>) называется ещё <i>конструктором</i>: она инициализирует объект, создавая его в памяти компьютера, и задаёт начальные значения всем его переменным (называемым ещё <i>состояниями</i> объекта). В 93-й строке (см. её повыше) как раз и вызывается этот конструктор для создания нового объекта-экрана, с которым и будет связана дальнейшая работа.</p>

<p align="jusify">А метод <code>__str__(self)</code> вызывается при печатании объекта-экрана:<br></p>
  <p align="center"><code><i>110:</i> print(screen)</code></p>
  
<p align="jusify">И ещё один момент! Надо всегда учитывать, что переменные в Python хранят в себе не сами списки, а ссылки на них. И присваивание значения-списка одной переменной другой — не создаст новую независимую копию списка, а скопирует ссылку на тот же самый список. Просмотрите и поймите такой код:</p>
  <table align="center"><tr><td>
    <p align="center"><code>names = [ [<b>"Киря"</b>, <b>"Вадик"</b>, <b>"Лёха"</b>], [<b>"Ваня"</b>, <b>"Лиза"</b>, <b>"Света"</b>] ]</code></p>
    <p align="center"><code>names[0] = names[1]</code></p>
    <p align="center"><code>names[1][0] = <b>"Ваааааняяяяяя!"</b></code></p>
    <p align="center"><code>print(names)</code></p>
  </td></tr></table>
  
<p align="jusify">Вопрос: а как будет выглядить этот список <code>names</code> при его печатании? Если Вы предположили, что так: <code>[ [<b>"Ваня"</b>, <b>"Лиза"</b>, <b>"Света"</b>], [<b>"Ваааааняяяяяя!"</b>, <b>"Лиза"</b>, <b>"Света"</b>] ]</code>, то Вы были не правы; если же Вы предположили так: <code>[ [<b>"Ваааааняяяяяя!"</b>, <b>"Лиза"</b>, <b>"Света"</b>], [<b>"Ваааааняяяяяя!"</b>, <b>"Лиза"</b>, <b>"Света"</b>] ]</code> — Вы попали в точку!</p>

<p align="jusify">И из-за этого свойства Python-списков был добавлен такой, поначалу, казалось бы, лишний, код:</p>
    <table align="center"><tr><td>
      <p align="center"><code>#==============================</code></p>
      <p align="center"><code># Эта конструкция обеспечивает создание новой строки, а не копирование ссылки на старую:</code></p>
      <p align="center"><code>self.__screen[0][col] = self.__screen[self.__height-1][col].split()</code></p>
      <p align="center"><code>self.__screen[0][col] = "".join(self.__screen[0][col])</code></p>
      <p align="center"><code>#==============================</code></p>
    </td></tr></table>

<h2 name="ans">Ответы к заданиям</h2>
<p align="jusify">
<table>
  <tr>
    <td></td><td colspan="5"><b>НОМЕР ЗАДАНИЯ</b></td>
  </tr>
  <tr>
    <td></td><td align="center"><b>1</b></td><td align="center"><b>2</b></td><td align="center"><b>3</b></td><td align="center"><b>4</b></td><td align="center"><b>5</b></td>
  </tr>
  <tr>
    <td><b>ОТВЕТ</b></td><td><img src="img/1.jpg"></img></td><td><img src="img/2.jpg"></img></td><td><img src="img/3.jpg"></img></td><td><img src="img/4.jpg"></img></td><td><img src="img/5.jpg"></img></td>
  </tr>
</table>
</p>
