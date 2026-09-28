# Awesome 1C MCP Servers

[![Check Links](https://github.com/Untru/1c-mcp/actions/workflows/links.yml/badge.svg)](https://github.com/Untru/1c-mcp/actions/workflows/links.yml)
[![Update Top](https://github.com/Untru/1c-mcp/actions/workflows/update-top.yml/badge.svg)](https://github.com/Untru/1c-mcp/actions/workflows/update-top.yml)

Каталог MCP-серверов, плагинов и наборов skills, которые подключают AI-ассистентов (Claude Code, Codex, Cursor, VS Code Copilot и др.) к 1С:Предприятие.

**Зачем это всё.** Сама по себе нейросеть про вашу 1С ничего не знает: не видит метаданные, путает методы платформы, не может запустить тест. [MCP](https://modelcontextprotocol.io) — стандартный «разъём», через который агенту дают инструменты: прочитать структуру конфигурации, найти процедуру, заглянуть в справку, выполнить запрос к базе, прогнать проверку. Skills — готовые инструкции, как этими инструментами пользоваться в типовых задачах 1С. Здесь собрано то, что для этого уже есть.

> **Что нового** — в [последнем релизе](https://github.com/Untru/1c-mcp/releases/latest) и [CHANGELOG.md](CHANGELOG.md).
> Нашли проект, которого тут нет? [Откройте issue](https://github.com/Untru/1c-mcp/issues/new?template=new-server.yml) или PR — см. [CONTRIBUTING.md](CONTRIBUTING.md).

## Содержание

- [Топ по звёздам](#топ-по-звёздам)
- [С чего начать](#с-чего-начать)
- [Каталог](#каталог)
  - [IDE-интеграции](#ide-интеграции)
  - [Живая база и фреймворки](#живая-база-и-фреймворки)
  - [Метаданные и анализ кода](#метаданные-и-анализ-кода)
  - [Справка платформы](#справка-платформы)
  - [Проверка кода и тестирование](#проверка-кода-и-тестирование)
  - [UI-тестирование и агент в интерфейсе](#ui-тестирование-и-агент-в-интерфейсе)
  - [1С:Напарник](#1снапарник)
  - [Учётные системы и данные](#учётные-системы-и-данные)
  - [Инфраструктура и DevOps](#инфраструктура-и-devops)
  - [1C:Element](#1celement)
  - [Плагины, правила и skills](#плагины-правила-и-skills)
  - [Коммерческие продукты](#коммерческие-продукты)
- [Типовые связки](#типовые-связки)

## Топ по звёздам

Open-source проекты каталога по числу звёзд на GitHub. Таблица пересобирается автоматически каждый понедельник ([workflow](.github/workflows/update-top.yml), [скрипт](scripts/update_top.py)).

<!-- TOP:START -->
| # | Проект | ⭐ | Что это | Раздел | Последний коммит |
|--:|--------|--:|---------|--------|------------------|
| 1 | [cc-1c-skills](https://github.com/Nikolay-Shirokov/cc-1c-skills) | 643 | Самый популярный набор skills для 1С: полный цикл разработки для Claude Code, Cursor и Codex | [Плагины, правила и skills](#плагины-правила-и-skills) | 2026-09-28 |
| 2 | [1c_mcp](https://github.com/vladimir-kharin/1c_mcp) | 518 | Фреймворк, чтобы сделать MCP-сервер из самой базы 1С | [Живая база и фреймворки](#живая-база-и-фреймворки) | 2026-09-27 |
| 3 | [ai_rules_1c](https://github.com/comol/ai_rules_1c) | 466 | Правила, субагенты и skills для AI-разработки на 1С — для любого агента | [Плагины, правила и skills](#плагины-правила-и-skills) | 2026-09-27 |
| 4 | [EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | 289 | Плагин, который открывает AI-агенту рабочее пространство 1C:EDT | [IDE-интеграции](#ide-интеграции) | 2026-09-27 |
| 5 | [1c-mcp-toolkit](https://github.com/ROCTUP/1c-mcp-toolkit) | 279 | Живая база для агента за пять минут — просто открыть обработку | [Живая база и фреймворки](#живая-база-и-фреймворки) | 2026-07-24 |
| 6 | [mcp-1c](https://github.com/feenlace/mcp-1c) | 233 | Один Go-бинарник, который даёт агенту и живую базу, и поиск по коду | [Метаданные и анализ кода](#метаданные-и-анализ-кода) | 2026-09-26 |
| 7 | [Unica](https://github.com/IngvarConsulting/unica) | 205 | Плагин для Claude Code и Codex: skills плюс собственный MCP runtime для 1С | [Плагины, правила и skills](#плагины-правила-и-skills) | 2026-09-28 |
| 8 | [rlm-tools-bsl](https://github.com/Dach-Coin/rlm-tools-bsl) | 198 | Анализ огромных конфигураций (ERP, УХ) без RAG и без траты токенов на чтение файлов | [Метаданные и анализ кода](#метаданные-и-анализ-кода) | 2026-09-28 |
| 9 | [mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context) | 196 | Синтакс-помощник для AI — чтобы агент перестал выдумывать методы платформы | [Справка платформы](#справка-платформы) | 2026-03-10 |
| 10 | [mcp-1c-v1](https://github.com/fserg/mcp-1c-v1) | 166 | RAG по структуре конфигурации: «найди, где хранится X» на естественном языке | [Метаданные и анализ кода](#метаданные-и-анализ-кода) | 2025-08-04 |
| 11 | [CodePilot1C](https://github.com/ondysss/codepilot1c-edt) | 153 | AI-ассистент, встроенный прямо в EDT: чат, агентный режим и MCP Host | [IDE-интеграции](#ide-интеграции) | 2026-09-25 |
| 12 | [code-index-mcp](https://github.com/Regsorm/code-index-mcp) | 130 | Быстрый индекс кода для агента: один бинарник, SQLite, ответ за миллисекунды | [Метаданные и анализ кода](#метаданные-и-анализ-кода) | 2026-09-28 |
| 13 | [mcp-onec-test-runner](https://github.com/alkoleft/mcp-onec-test-runner) | 113 | METR — агент сам запускает YaXUnit-тесты, сборку и синтакс-контроль | [Проверка кода и тестирование](#проверка-кода-и-тестирование) | 2026-03-22 |
| 14 | [1c-buddy](https://github.com/ROCTUP/1c-buddy) | 102 | Веб-чат, MCP-сервер и OpenAI-совместимый шлюз к Напарнику | [1С:Напарник](#1снапарник) | 2026-08-09 |
| 15 | [1c-mcp-metacode](https://github.com/ROCTUP/1c-mcp-metacode) | 102 | Конфигурация в виде графа в Neo4j: объекты, модули, процедуры и связи между ними | [Метаданные и анализ кода](#метаданные-и-анализ-кода) | 2026-08-19 |
<!-- TOP:END -->

## С чего начать

| Задача | Смотрите |
|--------|----------|
| Работать из 1C:EDT | [EDT-MCP](#edt-mcp), [edt-bridge](#edt-bridge), [CodePilot1C](#codepilot1c) |
| Работать из VS Code / Cursor | [1C: Platform Tools MCP](#1c-platform-tools-mcp), [плагины и skills](#плагины-правила-и-skills) |
| Быстро подключить живую базу | [mcp-1c](#mcp-1c), [1c-mcp-toolkit](#1c-mcp-toolkit) |
| Написать свой MCP-сервер внутри 1С | [1c_mcp](#1c_mcp), [http1c](#http1c) |
| Разобраться в большой конфигурации | [rlm-tools-bsl](#rlm-tools-bsl), [code-index-mcp](#code-index-mcp), [1c-mcp-metacode](#1c-mcp-metacode) |
| Справка по платформе и BSL | [mcp-bsl-platform-context](#mcp-bsl-platform-context), [onec-help-mcp](#onec-help-mcp) |
| Проверять код и гонять тесты | [bsl-analyzer](#bsl-analyzer), [mcp-onec-test-runner](#mcp-onec-test-runner), [v8-runner](#v8-runner) |
| Дать агенту прокликать интерфейс 1С | [1C Testpilot](#1c-testpilot) |
| Работать с данными учёта | [aprovodka](#aprovodka), [mcp-rsv-data](#mcp-rsv-data), [ARQA](#коммерческие-продукты) |
| Готовые skills для Claude Code / Codex / Cursor | [cc-1c-skills](#cc-1c-skills), [Unica](#unica), [ai_rules_1c](#ai_rules_1c), [claude-code-skills-1c](#claude-code-skills-1c) |

## Каталог

Строка под названием: стек · транспорт MCP · требования · статус.
Статусы: ✅ стабилен и развивается · 🚧 бета, API может меняться · 🔬 эксперимент · 📦 не поддерживается.

### IDE-интеграции

#### [EDT-MCP](https://github.com/DitriXNew/EDT-MCP)

**Плагин, который открывает AI-агенту рабочее пространство 1C:EDT.**
Агент видит проект так же, как вы в IDE: ходит по метаданным и модулям, строит иерархию вызовов, получает подсказки Content Assist, проверяет текст запроса (включая режим СКД), снимает скриншоты форм, обновляет базу и запускает отладку. Главный выбор, если вы живёте в EDT и хотите, чтобы агент опирался на её понимание кода, а не на grep по файлам.

С версии 2.18 умеет ещё и создать EDT-проект из `.cf`/`.cfe`/`.epf`/`.erf` и выгрузить конфигурацию обратно в `.cf`/`.cfe`.

Java · HTTP, SSE · EDT 2025.2+ · ✅ ![stars](https://img.shields.io/github/stars/DitriXNew/EDT-MCP?style=flat&label=%E2%AD%90)

#### [edt-bridge](https://github.com/keyfire/edt-bridge)

**Живая семантическая модель EDT для агента — не только чтение, но и запись.**
Агент спрашивает не файлы, а запущенную IDE: реальные ошибки валидации EDT, типы метаданных, перекрёстные ссылки, проверку запроса по метаданным проекта, синтакс-помощник. Плюс инструменты записи и рефакторинга, работа с ИБ и отладчик. Запись защищена токеном и сначала возвращает план. Автор — тот же, что у elemctl и xbsl.

Java · HTTP (localhost) · EDT · 🚧 ![stars](https://img.shields.io/github/stars/keyfire/edt-bridge?style=flat&label=%E2%AD%90)

#### [AI-EDT](https://github.com/Desko77/ai-edt)

**MCP-сервер внутри EDT, который отвечает на вопросы «что от чего зависит».**
Какие формы, роли и подсистемы используют справочник, на какой объект указывает ссылка — всё через семантическую модель EDT, а не поиском по XML. Есть валидация и живая отладка. Работает в паре с [claude-code-skills-1c](#claude-code-skills-1c) того же автора. EDT 2026.1–2026.2.

Java · HTTP · EDT 2026.1+ · 🚧 ![stars](https://img.shields.io/github/stars/Desko77/ai-edt?style=flat&label=%E2%AD%90)

#### [1C_EDT_MCP_PUBLIC](https://github.com/fedukhin-sys/1C_EDT_MCP_PUBLIC)

**Плагин EDT со 106 MCP-инструментами — самый широкий охват IDE.**
Workspace, модули, метаданные, формы, СКД, информационные базы (включая синхронизацию `.dt`/`.cfe`), журнал регистрации, отладка, запуск клиента и xUnitFor1C. Внимание: у репозитория нет лицензии, для коммерческого использования уточняйте у автора.

Java · HTTP, SSE · EDT 2023.x–2026.x · 🚧 ![stars](https://img.shields.io/github/stars/fedukhin-sys/1C_EDT_MCP_PUBLIC?style=flat&label=%E2%AD%90)

#### [CodePilot1C](https://github.com/ondysss/codepilot1c-edt)

**AI-ассистент, встроенный прямо в EDT: чат, агентный режим и MCP Host.**
Не сервер для внешнего агента, а сам агент внутри IDE. Работает с BSL AST, формами и метаданными, умеет запускать QA-команды и подключать сторонние MCP-серверы. Можно подставить свою модель. Удобен тем, кто не хочет выходить из EDT в терминал.

Java · MCP Host · EDT, JDK 17 · ✅ ![stars](https://img.shields.io/github/stars/ondysss/codepilot1c-edt?style=flat&label=%E2%AD%90)

#### [1C: Platform Tools MCP](https://github.com/yellow-hammer/mcp-1c-platform-tools)

**MCP-обёртка над VS Code-расширением [1C: Platform Tools](https://marketplace.visualstudio.com/items?itemName=yellow-hammer.1c-platform-tools).**
Всё, что расширение умеет делать с проектом 1С (сборка, выгрузка, запуск и т. п.), становится доступным агенту в Cursor, VS Code или любом MCP-клиенте. С версии 0.3 — ещё и запросы к данным базы через OData. Для тех, кто ведёт 1С-проекты в VS Code, а не в EDT.

TypeScript · stdio · VS Code/Cursor + расширение · ✅ ![stars](https://img.shields.io/github/stars/yellow-hammer/mcp-1c-platform-tools?style=flat&label=%E2%AD%90)

#### [BslEdit](https://github.com/alonehobo/BslEdit)

**Лёгкий редактор BSL и «глаза» для агента без запуска 1С.**
Standalone-редактор на Monaco, просмотр форм и макетов так, как они выглядят в Конфигураторе, отчёты проверок кода и MCP-инструменты, чтобы агент мог «увидеть» форму. Ставится одной командой PowerShell и сам подключается к Claude Code, Codex и Cursor.

JavaScript · MCP · Windows · ✅ ![stars](https://img.shields.io/github/stars/alonehobo/BslEdit?style=flat&label=%E2%AD%90)

### Живая база и фреймворки

#### [1c_mcp](https://github.com/vladimir-kharin/1c_mcp)

**Фреймворк, чтобы сделать MCP-сервер из самой базы 1С.**
Ставите расширение `MCP_Сервер.cfe` — вся механика протокола уже внутри. Вам остаётся на BSL описать свои инструменты (`ДобавитьИнструменты()` / `ВыполнитьИнструмент()`), и агент сможет вызывать вашу бизнес-логику. Поддерживает resources и prompts, подключается напрямую по HTTP, через Python-прокси (stdio + OAuth2) или в Docker. Самый популярный проект каталога.

BSL, Python · HTTP, stdio · 8.3+ · ✅ ![stars](https://img.shields.io/github/stars/vladimir-kharin/1c_mcp?style=flat&label=%E2%AD%90)

#### [1c-mcp-toolkit](https://github.com/ROCTUP/1c-mcp-toolkit)

**Живая база для агента за пять минут — просто открыть обработку.**
HTTP-сервер поднимается прямо внутри `.epf`: не нужно менять конфигурацию, публиковать базу на веб-сервере или возиться с COM. Агент выполняет запросы и код, читает метаданные, журнал регистрации и объекты по ссылке. Есть REST API для агентов без MCP, анонимизация чувствительных данных и готовые skills. Хороший вариант «подключиться к клиентской базе и посмотреть».

BSL, Python · HTTP · 8.2.13+ · ✅ ![stars](https://img.shields.io/github/stars/ROCTUP/1c-mcp-toolkit?style=flat&label=%E2%AD%90)

#### [http1c](https://mcpmarket.com/server/http1c)

**Нативная компонента + шаблон обработки для публикации бизнес-логики 1С как MCP-сервера.**
Транспорт вынесен в DLL, поэтому из 1С можно динамически регистрировать tools, resources и prompts с bearer-авторизацией, проверкой origin, rate limiting и пагинацией. Для тех, кому нужен полноценный протокол, а не минимальная обёртка.

BSL, C++ · HTTP, SSE · ✅

#### [ИИкона (1c-ai-connector)](https://github.com/andromanpro/1c-ai-connector)

**ИИ-платформа внутри 1С, которая ставится расширением.**
Не только MCP-сервер для внешних агентов, но и агентская петля с function calling к пяти+ провайдерам (OpenAI, Anthropic, Google, DeepSeek, GigaChat, Yandex), RAG по базе знаний на Qdrant, мониторинг ошибок с ИИ-диагнозом и алертами в Telegram, генератор диаграмм. Подходит, когда AI нужен пользователям самой 1С, а не только разработчику.

BSL · HTTP · 8.3.24+, БСП 3.1.10+ · ✅ ![stars](https://img.shields.io/github/stars/andromanpro/1c-ai-connector?style=flat&label=%E2%AD%90)

#### [onec-client-mcp-devkit](https://github.com/1c-neurofish/onec-client-mcp-devkit)

**MCP-сервер, который живёт прямо в клиенте 1С:Предприятие.**
Расширение поднимает сервер в клиентском контуре через внешнюю компоненту WebTransport: агенту доступны tools, resources и prompts от имени открытого сеанса пользователя. На нём, например, строят «ИИ-оператора», который работает в интерфейсе вместо человека. Стабильного релиза пока нет.

BSL · WebTransport · 🚧 ![stars](https://img.shields.io/github/stars/1c-neurofish/onec-client-mcp-devkit?style=flat&label=%E2%AD%90)

#### [v8-session-manager](https://github.com/1c-neurofish/v8-session-manager)

**Собирает инструменты нескольких открытых клиентов 1С в один MCP endpoint.**
Клиенты 1С подключаются по WebSocket и публикуют свои tools (например, через [onec-client-mcp-devkit](#onec-client-mcp-devkit)), а агент видит их единым списком с префиксами по сессиям. Нужен, когда агент должен работать с несколькими базами или сеансами одновременно.

Rust · HTTP · 🚧 ![stars](https://img.shields.io/github/stars/1c-neurofish/v8-session-manager?style=flat&label=%E2%AD%90)

### Метаданные и анализ кода

#### [mcp-1c](https://github.com/feenlace/mcp-1c)

**Один Go-бинарник, который даёт агенту и живую базу, и поиск по коду.**
Подключается к HTTP-сервису 1С (расширение ставит сам): метаданные, формы, запросы с параметрами, журнал регистрации. Если рядом лежит выгрузка конфигурации — ищет по BSL (BM25, regex, точное совпадение). Без Python, Docker и прочего рантайма — скачал и запустил.

Go · stdio · 8.3+ · ✅ ![stars](https://img.shields.io/github/stars/feenlace/mcp-1c?style=flat&label=%E2%AD%90)

#### [rlm-tools-bsl](https://github.com/Dach-Coin/rlm-tools-bsl)

**Анализ огромных конфигураций (ERP, УХ) без RAG и без траты токенов на чтение файлов.**
Вместо того чтобы агент сам читал тысячи модулей, он пишет короткие скрипты в песочнице с 60+ хелперами поверх SQLite-индекса методов и графа вызовов. Понимает CF, EDT, CFE, MDO и кириллицу. Хорош для вопросов «как устроен этот механизм» и «где это вызывается».

Python · HTTP, stdio · платформа не нужна · ✅ ![stars](https://img.shields.io/github/stars/Dach-Coin/rlm-tools-bsl?style=flat&label=%E2%AD%90)

#### [code-index-mcp](https://github.com/Regsorm/code-index-mcp)

**Быстрый индекс кода для агента: один бинарник, SQLite, ответ за миллисекунды.**
Разбирает выгрузки Конфигуратора и EDT (конфигурация на 88 тыс. файлов индексируется минут за шесть) и даёт 32 инструмента: 20 универсальных на tree-sitter для 14 языков и 12 специально под 1С/BSL. Ставится одной командой, без Python и Docker. Хорош, когда агенту нужно быстро найти «где объявлено» и «кто вызывает» в большой конфигурации.

Rust · stdio · платформа не нужна · ✅ ![stars](https://img.shields.io/github/stars/Regsorm/code-index-mcp?style=flat&label=%E2%AD%90)

#### [gyrfalcon](https://github.com/aleksandrgradoboev-svg/gyrfalcon)

**Детерминированный индекс конфигурации: код, метаданные и граф вызовов в одном бинарнике.**
Конфигурацию на 18 000+ модулей индексирует примерно за минуту, дальше обновляется по изменённым файлам и сам отмечает, если ответ устарел. Каждая связь в графе вызовов помечена, насколько уверенно она распознана, поэтому «не смогли разрешить» отличается от «разрешать нечего». Знает 27 видов метаданных (реквизиты с типами, права ролей, подписки, регламентные задания, движения регистров, XDTO), перехваты расширений с местом вставки и офлайн-семантический поиск по именам. Один сервер держит несколько конфигураций.

Rust · stdio · XML-выгрузка, Windows x64 · 🚧 ![stars](https://img.shields.io/github/stars/aleksandrgradoboev-svg/gyrfalcon?style=flat&label=%E2%AD%90)

#### [bsl-atlas](https://github.com/Arman-Kudaibergenov/bsl-atlas)

**Индекс и поиск по исходникам 1С: процедуры, метаданные, связи и граф вызовов.**
Работает с XML/BSL-выгрузкой конфигурации или расширения. Режим `fast` — структурный поиск через SQLite/FTS без внешних embedding API, полный режим добавляет векторный поиск. Переиндексация после новой выгрузки.

Python · MCP · Docker · ✅ ![stars](https://img.shields.io/github/stars/Arman-Kudaibergenov/bsl-atlas?style=flat&label=%E2%AD%90)

#### [1c-mcp-metacode](https://github.com/ROCTUP/1c-mcp-metacode)

**Конфигурация в виде графа в Neo4j: объекты, модули, процедуры и связи между ними.**
Грузит метаданные прямо из XML-выгрузки (можно по расписанию), учитывает расширения, строит граф вызовов, делает семантический поиск по BSL и AI-саммари объектов. С версии 2.0 — 22 типизированных инструмента и веб-консоль со встроенным агентом. Для тех, кому нужен «гугл по конфигурации» для всей команды.

Python · stdio · Neo4j · ✅ ![stars](https://img.shields.io/github/stars/ROCTUP/1c-mcp-metacode?style=flat&label=%E2%AD%90)

#### [bsl-graph](https://github.com/alkoleft/bsl-graph)

**Граф знаний конфигурации в NebulaGraph с интерактивной визуализацией.**
Разбирает выгрузку Конфигуратора или EDT и позволяет и человеку (веб-интерфейс на Sigma.js), и агенту (MCP) исследовать связи между объектами. Не обновлялся с осени 2025.

Kotlin · MCP, REST · JDK 17, NebulaGraph · 🚧 ![stars](https://img.shields.io/github/stars/alkoleft/bsl-graph?style=flat&label=%E2%AD%90)

#### [mcp-1c-v1](https://github.com/FSerg/mcp-1c-v1)

**RAG по структуре конфигурации: «найди, где хранится X» на естественном языке.**
Обработка выгружает структуру, Docker Compose поднимает Qdrant, эмбеддинги, загрузчик и MCP-сервер. Один из первых проектов в нише, давно не обновлялся.

TypeScript · HTTP · Docker · 🚧 ![stars](https://img.shields.io/github/stars/FSerg/mcp-1c-v1?style=flat&label=%E2%AD%90)

#### [1C_MCP_metadata](https://github.com/artesk/1C_MCP_metadata)

**Метаданные конфигурации через расширение с HTTP-сервисом и PowerShell-мостом.**
Структура, поиск по имени/синониму и проверка текста запроса. Минималистичный вариант без Python и Docker. Не обновлялся с 2025 года.

BSL, PowerShell · stdio · 8.3+ · 🚧 ![stars](https://img.shields.io/github/stars/artesk/1C_MCP_metadata?style=flat&label=%E2%AD%90)

#### [1c-templates-mcp](https://yellowmcp.com/servers/1c-templates-mcp)

**Библиотека из 2200+ шаблонов BSL-кода с семантическим поиском.**
Агент ищет готовую заготовку («отправка почты», «запись в регистр») вместо того чтобы сочинять с нуля. Шаблоны можно редактировать в веб-интерфейсе.

Python · SSE · Docker, ChromaDB · ✅

### Справка платформы

#### [mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)

**Синтакс-помощник для AI — чтобы агент перестал выдумывать методы платформы.**
Нечёткий поиск по типам, методам, свойствам и конструкторам, данные берутся из установленной платформы. Подключается первым делом почти в любой связке.

Kotlin · stdio, SSE · JDK 17, 8.3.20+ · ✅ ![stars](https://img.shields.io/github/stars/alkoleft/mcp-bsl-platform-context?style=flat&label=%E2%AD%90)

#### [bsl-context](https://github.com/Regsorm/bsl-context)

**Справка платформы плюс проверка, что агент не выдумал метод или значение перечисления.**
Берёт данные из синтакс-помощника платформы (`shcntx_ru.hbk`, запускать 1С не нужно) и умеет статически проверять BSL-выражения по реальному индексу: существует ли такой метод у типа, есть ли такое системное перечисление. Ловит именно те галлюцинации, которые линтер пропускает.

Rust · MCP · 🚧 ![stars](https://img.shields.io/github/stars/Regsorm/bsl-context?style=flat&label=%E2%AD%90)

#### [mcp-bsl-platform-help-context](https://github.com/Desko77/mcp-bsl-platform-help-context)

**Python-порт mcp-bsl-platform-context с гибридным поиском и стандартами кода.**
Keyword, semantic (Qdrant) и hybrid-поиск по API платформы, документация по строгой типизации BSL и стилю, автоопределение версии платформы. Не требует Java.

Python · stdio, SSE, HTTP · ✅ ![stars](https://img.shields.io/github/stars/Desko77/mcp-bsl-platform-help-context?style=flat&label=%E2%AD%90)

#### [onec-help-mcp](https://github.com/rzateev/onec-help-mcp)

**Поиск по официальной справке нескольких версий платформы (BM25 + семантика).**
Отвечает и на точные запросы по имени метода, и на вопросы «как сделать X». Есть REST API для скриптов.

Python · MCP, REST · Docker, Qdrant · ✅ ![stars](https://img.shields.io/github/stars/rzateev/onec-help-mcp?style=flat&label=%E2%AD%90)

#### [1c-syntax-helper-mcp](https://github.com/Antonio1C/1c-syntax-helper-mcp)

**Справка из `.hbk`-файла платформы на Elasticsearch — один сервер на всю команду.**
Поднимается в Docker, держит десяток одновременных пользователей.

Python · HTTP · Docker, Elasticsearch · ✅ ![stars](https://img.shields.io/github/stars/Antonio1C/1c-syntax-helper-mcp?style=flat&label=%E2%AD%90)

### Проверка кода и тестирование

#### [bsl-analyzer](https://github.com/itrous/bsl-analyzer)

**Быстрый анализатор BSL на Rust: линтер, LSP и MCP в одном бинарнике.**
180 диагностик, LSP для VS Code/Cursor/Zed, CLI с отчётами SARIF/JSONL для CI и MCP-профили для справки и работы с проектом. Агент может сам проверить только что написанный код, не дожидаясь EDT.

Rust · stdio, LSP · платформа не нужна · 🚧 ![stars](https://img.shields.io/github/stars/itrous/bsl-analyzer?style=flat&label=%E2%AD%90)

#### [mcp-onec-test-runner](https://github.com/alkoleft/mcp-onec-test-runner)

**METR — агент сам запускает YaXUnit-тесты, сборку и синтакс-контроль.**
Работает с форматами Конфигуратора и EDT, умеет быстро конвертировать через EDT CLI. Замыкает цикл «написал → проверил → исправил» без человека.

Kotlin · stdio · JDK 17, 8.3.10+, YaXUnit · ✅ ![stars](https://img.shields.io/github/stars/alkoleft/mcp-onec-test-runner?style=flat&label=%E2%AD%90)

#### [mcp-bsl-lsp-bridge](https://github.com/SteelMorgan/mcp-bsl-lsp-bridge)

**Мост к BSL Language Server: навигация, символы, 100+ диагностик и рефакторинг через MCP.**
Если BSL LS у вас уже настроен — это самый короткий путь дать его возможности агенту.

MCP · BSL LS · 🚧 ![stars](https://img.shields.io/github/stars/SteelMorgan/mcp-bsl-lsp-bridge?style=flat&label=%E2%AD%90)

#### [bsl-mcp](https://github.com/phsin/mcp-bsl-ls)

**Проверка и форматирование `.bsl`/`.os` через BSL Language Server с ответом в JSON.**
Простой линтер для агента: файл или каталог на вход — список ошибок на выходе. Не обновлялся с ноября 2025.

Python · stdio · JRE, BSL LS · ✅ ![stars](https://img.shields.io/github/stars/phsin/mcp-bsl-ls?style=flat&label=%E2%AD%90)

#### [1c-lsp-mcp-skill](https://github.com/fserg/1c-lsp-mcp-skill)

**Менеджер нескольких BSL Language Server сразу — по одному на каждый проект.**
Запускает инстансы BSL LS с прогрессом индексации, отдаёт диагностику и навигацию (символы, ссылки, входящие/исходящие вызовы) через MCP или CLI для skills. Без Docker, нужна только JVM.

Rust · MCP, CLI · JVM, BSL LS · 🚧 ![stars](https://img.shields.io/github/stars/fserg/1c-lsp-mcp-skill?style=flat&label=%E2%AD%90)

#### [PRISM](https://github.com/genlab-1c/prism)

**Открытый бенчмарк: какая нейросеть лучше пишет код на 1С.**
Не MCP-сервер, но полезен при выборе модели для агента. Код, сгенерированный Claude, GPT, Gemini, DeepSeek, YandexGPT и GigaChat, реально исполняется в 1С и оценивается по синтаксису, смыслу, оптимальности и использованию платформы. Результаты на [prism.genlab-1c.ru](https://prism.genlab-1c.ru), датасет на HuggingFace.

Python · бенчмарк · ✅ ![stars](https://img.shields.io/github/stars/genlab-1c/prism?style=flat&label=%E2%AD%90)

### UI-тестирование и агент в интерфейсе

Агент открывает формы, заполняет поля и проверяет результат в настоящем клиенте 1С — через штатный клиент тестирования (`/TESTCLIENT`), без Vanessa Automation.

#### [1C Testpilot](https://github.com/ROCTUP/1c-testpilot)

**Агент кликает по интерфейсу 1С сам: открывает формы, заполняет документы, проверяет результат.**
MCP-сервер напрямую подключается к клиенту тестирования 1С по его сетевому протоколу, без менеджера тестирования и без Vanessa. Может сам запустить тест-клиент (файловая или серверная база), ходить по дереву окно → форма → элементы, читать и заполнять поля, таблицы и табличные документы, делать снимки формы и сравнивать состояния, снимать скриншоты окна, не отбирая фокус. Умеет записывать и воспроизводить сценарии (uilog) и дружит с pytest. Опционально — выполнение BSL-кода и запросов через обработку. Автор 1c-mcp-toolkit и 1c-buddy, проект вышел в сентябре 2026 и быстро развивается.

Python · stdio, HTTP · 8.3.27+ / 8.5 · ✅ ![stars](https://img.shields.io/github/stars/ROCTUP/1c-testpilot?style=flat&label=%E2%AD%90)

#### [qa-mcp](https://github.com/vlikhobabin/qa-mcp-public)

**QA-менеджер и MCP-сервер на нативном протоколе TestManager/TestClient.**
Гоняет BDD/Gherkin-сценарии, читает и проверяет управляемые формы, выдаёт отчёты JUnit/Allure — всё без рантайма Vanessa. Публичный MVP, автор прямо пишет, что не стабилен.

Python · MCP · 🔬 ![stars](https://img.shields.io/github/stars/vlikhobabin/qa-mcp-public?style=flat&label=%E2%AD%90)

### 1С:Напарник

Серверы, которые дают внешнему агенту доступ к [1С:Напарнику](https://code.1c.ai) — официальной нейросети 1С, обученной на типовых и стандартах. Нужен токен (подписка ИТС).

#### [1c-ai-mcp](https://github.com/Desko77/1c-ai-mcp)

**Самая полная обёртка над Напарником: 12 инструментов.**
Проверка, ревью, переписывание и доработка кода, поиск по ИТС и справке, сравнение версий документации. Режим Direct вызывает инструменты Напарника напрямую, а не через текстовый промпт.

Python · HTTP, SSE · Docker · ✅ ![stars](https://img.shields.io/github/stars/Desko77/1c-ai-mcp?style=flat&label=%E2%AD%90)

#### [1c-buddy](https://github.com/ROCTUP/1c-buddy)

**Веб-чат, MCP-сервер и OpenAI-совместимый шлюз к Напарнику.**
Можно подключить Напарника как «модель» в любой инструмент, который умеет OpenAI API.

JS, Python · MCP, OpenAI API · Docker · ✅ ![stars](https://img.shields.io/github/stars/ROCTUP/1c-buddy?style=flat&label=%E2%AD%90)

#### [spring-mcp-1c-copilot](https://github.com/SteelMorgan/spring-mcp-1c-copilot)

**MCP-сервер к Напарнику на Spring Boot со Swagger UI.**

Kotlin · SSE · JDK 17 · 🚧 ![stars](https://img.shields.io/github/stars/SteelMorgan/spring-mcp-1c-copilot?style=flat&label=%E2%AD%90)

### Учётные системы и данные

#### [aprovodka](https://github.com/theYahia/aprovodka)

**Агент читает и пишет данные учёта через штатный OData — без расширений и BSL.**
Бывший `1c-rest-mcp`. 34 инструмента: справочники, документы, регистры, бухгалтерия, пакетные операции, отслеживание изменений. Запуск одной командой `npx -y @theyahia/aprovodka`. Подходит для аналитики и операций с данными, когда OData уже опубликован.

TypeScript · stdio, HTTP · Node.js 18+, OData · ✅ ![stars](https://img.shields.io/github/stars/theYahia/aprovodka?style=flat&label=%E2%AD%90)

#### [mcp-rsv-data](https://github.com/prepod2003/mcp-rsv-data)

**Бухгалтер спрашивает словами — агент отвечает цифрами из рабочей базы.**
«Покажи остатки по складам», «сколько продали такого-то товара» — без знания языка запросов. Только чтение, права пользователя соблюдаются, персональные данные обезличиваются автоматически. Заодно отдаёт разработчику точную структуру метаданных любой конфигурации. Ставится расширением, базу не меняет.

Go, BSL · stdio · ✅ ![stars](https://img.shields.io/github/stars/prepod2003/mcp-rsv-data?style=flat&label=%E2%AD%90)

#### [INFATON MCP35](https://github.com/infaton/MCP35)

**MCP-сервер на стороне 1С:ERP с 90+ инструментами.**
Движок, на котором INFATON строит «цифровых двойников» и AI-агентов над ERP. Открыт под MIT — можно встроить в свой продукт.

BSL · HTTP (JSON-RPC) · 1С:ERP · ✅ ![stars](https://img.shields.io/github/stars/infaton/MCP35?style=flat&label=%E2%AD%90)

#### [1c-accounting-mcp](https://github.com/tarasov46/1c-accounting-mcp)

**Интеграция AI с 1С:Бухгалтерией.** Ранний прототип, давно без обновлений.

Python, JS · stdio · 🔬 ![stars](https://img.shields.io/github/stars/tarasov46/1c-accounting-mcp?style=flat&label=%E2%AD%90)

### Инфраструктура и DevOps

#### [v8-runner](https://github.com/alkoleft/v8-runner-rust)

**Весь локальный цикл разработки одной командой — и безопасный MCP для агента.**
Один `v8project.yaml` описывает исходники, рабочую базу и тесты; дальше v8-runner сам собирает (Designer или IBCMD), готовит ИБ, гоняет синтакс-контроль, YaXUnit и Vanessa и выгружает изменения обратно. Агенту отдаётся ограниченный набор из 8 инструментов вместо доступа к shell.

Rust · stdio, HTTP · Designer/IBCMD · 🚧 ![stars](https://img.shields.io/github/stars/alkoleft/v8-runner-rust?style=flat&label=%E2%AD%90)

#### [1c-log-checker](https://github.com/SteelMorgan/1c-log-checker)

**Журнал регистрации и технологический журнал в ClickHouse + Grafana, с доступом для агента.**
Агент сам ищет ошибки и узкие места в логах и может настроить сбор ТЖ.

MCP · Docker, ClickHouse · 🚧 ![stars](https://img.shields.io/github/stars/SteelMorgan/1c-log-checker?style=flat&label=%E2%AD%90)

#### [1c-ai-sandbox](https://github.com/SteelMorgan/1c-ai-sandbox-client-server)

**Docker-песочница с полным окружением 1С, чтобы агент экспериментировал, не трогая прод.**

Docker · 🔬 ![stars](https://img.shields.io/github/stars/SteelMorgan/1c-ai-sandbox-client-server?style=flat&label=%E2%AD%90)

#### [compose4mcp](https://github.com/pravets/compose4mcp)

**Готовые Docker Compose для набора MCP-серверов 1С.**
Поиск по коду и метаданным, справка, синтакс-проверка, БСП, шаблоны, Напарник — поднимаются одной командой. Не обновлялся с осени 2025.

Docker Compose · ✅ ![stars](https://img.shields.io/github/stars/pravets/compose4mcp?style=flat&label=%E2%AD%90)

<a id="1celement"></a>

### 1C:Element

Облачная платформа 1С ([1cmycloud.com](https://1cmycloud.com)) с языком XBSL. Инструменты ниже неофициальные и с 1С не аффилированы.

#### [elemctl](https://github.com/keyfire/elemctl)

**CLI и MCP для деплоя приложений 1C:Element с честной проверкой результата.**
Собирает архив, загружает, применяет и отдельно проверяет, что деплой действительно прошёл: платформа молча откатывает неудачные. Ветки разработки, старт/стоп приложений.

Python · stdio · 🔬 ![stars](https://img.shields.io/github/stars/keyfire/elemctl?style=flat&label=%E2%AD%90)

#### [xbsl](https://github.com/keyfire/xbsl)

**Линтер, LSP и MCP для XBSL-кода.**
161 правило, расширение VS Code с дизайнером форм, скаффолдинг объектов и маршрутов без ручного YAML.

MCP, LSP · 🔬 ![stars](https://img.shields.io/github/stars/keyfire/xbsl?style=flat&label=%E2%AD%90)

#### [xbsl-ai-skills](https://github.com/korolevpavel/xbsl-ai-skills)

**20 skills для разработки на 1С:Элемент, сверенные с версией 10.0.**
Метаданные, формы, журнал данных, интегрируемые приложения, регистры, развёртывание. Работают в Claude Code и других агентах со skills.

Python · Claude Code и др. · ✅ ![stars](https://img.shields.io/github/stars/korolevpavel/xbsl-ai-skills?style=flat&label=%E2%AD%90)

### Плагины, правила и skills

Не MCP-серверы общего назначения, а готовые наборы знаний и инструментов для агента, часто поверх серверов из разделов выше. Ставятся один раз и сразу дают агенту «опыт» 1С-разработчика.

#### [cc-1c-skills](https://github.com/Nikolay-Shirokov/cc-1c-skills)

**Самый популярный набор skills для 1С: полный цикл разработки для Claude Code, Cursor и Codex.**
Даёт модели готовые абстракции над XML-форматами выгрузки и CLI Конфигуратора, чтобы агент работал с сутью задачи (объект, форма, роль, СКД), а не с тысячами строк XML. Плюс «глаза и руки» для проверки результата через веб-клиент. Установка — скопировать `.claude/skills/` в проект; есть версии на PowerShell и Python.

PowerShell, Python · Claude Code, Cursor, Codex · ✅ ![stars](https://img.shields.io/github/stars/Nikolay-Shirokov/cc-1c-skills?style=flat&label=%E2%AD%90)

#### [Unica](https://github.com/IngvarConsulting/unica)

**Плагин для Claude Code и Codex: skills плюс собственный MCP runtime для 1С.**
Агент создаёт и проверяет метаданные, формы, EPF/ERF, СКД, роли, запускает 1С и ищет по BSL через единый сервер `unica`. Ставится из marketplace, runtime скачивается с проверкой SHA-256. Windows, Linux, macOS.

Rust, Python · Claude Code, Codex · 8.3.27 для запуска 1С · ✅ ![stars](https://img.shields.io/github/stars/IngvarConsulting/unica?style=flat&label=%E2%AD%90)

#### [ai_rules_1c](https://github.com/comol/ai_rules_1c)

**Правила, субагенты и skills для AI-разработки на 1С — для любого агента.**
Бывший `cursor_rules_1c`. Стандарты кода, формы, запросы, тестирование, каталог антипаттернов, 13 субагентов и диспетчер MCP-инструментов. Работает в Cursor, Claude Code, Codex, OpenCode, Cline и ещё десятке инструментов, ставится скриптом.

Markdown · 11+ агентов · ✅ ![stars](https://img.shields.io/github/stars/comol/ai_rules_1c?style=flat&label=%E2%AD%90)

#### [claude-code-skills-1c](https://github.com/Desko77/claude-code-skills-1c)

**117 skills для Claude Code: агент собирает исходники 1С из компактного JSON, а не правит XML руками.**
Метаданные, формы, расширения, роли, СКД, макеты, обработки плюс 14 валидаторов и единый индекс конфигурации для перекрёстных проверок. Базовая генерация работает офлайн без платформы.

PowerShell, Python · Claude Code · ✅ ![stars](https://img.shields.io/github/stars/Desko77/claude-code-skills-1c?style=flat&label=%E2%AD%90)

#### [cursor-1c-skills](https://github.com/Desko77/cursor-1c-skills)

**То же самое для Cursor:** 116 skills и 40 правил.

PowerShell, Python · Cursor · ✅ ![stars](https://img.shields.io/github/stars/Desko77/cursor-1c-skills?style=flat&label=%E2%AD%90)

#### [1c-ai-dev-env](https://github.com/Pradushkoai/1c-ai-dev-env)

**Готовая среда 1С-разработки с AI: справочники, правила и MCP в одном репозитории.**
BM25-поиск по методам, API-справочники на 100+ тыс. методов, BSL LS, 261 правило стандартов, MCP-сервер на 8 инструментов и компактный `AGENTS.md` с правилами, «рождёнными реальными инцидентами».

BSL, Python · Cursor, Claude, VS Code · ✅ ![stars](https://img.shields.io/github/stars/Pradushkoai/1c-ai-dev-env?style=flat&label=%E2%AD%90)

#### [1C: Platform Tools Skills](https://marketplace.visualstudio.com/items?itemName=yellow-hammer.1c-platform-tools)

**Skills, которые идут вместе с расширением 1C: Platform Tools.** Учат агента правильно вызывать команды расширения; работают в паре с [его MCP](#1c-platform-tools-mcp).

Cursor, Copilot, Claude · ✅

### Коммерческие продукты

| Продукт | Что это и зачем | Цена |
|---------|-----------------|------|
| [one-s-mcp](https://onesmcp.ru) | Десктоп-приложение с MCP-серверами: разбирает выгрузку, строит семантический индекс и граф вызовов, анализ влияния с учётом расширений, 190 диагностик, справка платформы и БСП. Всё локально | Открытая бета, бесплатно |
| [OneMCP](https://onemcp.ru) | SaaS: семантический поиск по метаданным, коду и документации для команды до 100 человек | Бета, бесплатно |
| [ARQA MCP Server](https://arqa.cc/ru/mcp-server) | On-premise MCP для бизнеса: создать счёт, найти контрагента, построить ОСВ словами (БП 3.0, УТ 11, ERP, ЗУП) | Платно, 14 дней бесплатно |
| [OneRPA MCP Suite](https://docs.onerpa.ru/mcp-servery-1c) | Набор Docker-серверов: справка, метаданные, граф, БСП, синтаксис, шаблоны, формы, Напарник | Платно |
| [Pilot 1C](https://infostart.ru/marketplace/2787345/) | ИИ-помощник от Инфостарта: пишет код и тесты в формате Vanessa Automation, работает в связке с Analyzer 1C и Insight 1C через MCP | От 18 300 ₽/мес. |
| [My1cMCP](https://infostart.ru/public/2782550/) | MCP-сервер на 22 функции: чтение и запись данных, выполнение BSL | 2 500 ₽ |
| [VibeCoding1C](http://vibecoding1c.ru) | Конструктор MCP-серверов без программирования и курсы | От 8 000 ₽ |
| [Infostart MCP](https://infostart.ru) | Поиск по метаданным, синтакс-помощник и проверка синтаксиса в Docker | Платно |

## Типовые связки

- **AI пишет обработку или расширение:** `mcp-1c` / `1c_mcp` (контекст базы) → `mcp-bsl-platform-context` (справка) → `bsl-analyzer` (диагностика) → `mcp-onec-test-runner` (YaXUnit).
- **Разобраться в большой конфигурации:** `rlm-tools-bsl` или `1c-mcp-metacode` + `onec-help-mcp`.
- **Code review BSL:** `bsl-analyzer` / `mcp-bsl-lsp-bridge` + `rlm-tools-bsl` + `1c-ai-mcp` (проверка Напарником).
- **Написал — проверь руками агента:** код через `mcp-onec-test-runner` / `v8-runner`, затем `1C Testpilot` открывает форму в тест-клиенте, заполняет документ и сверяет результат.
- **Локальный цикл без ручных кликов:** `v8-runner` (сборка, ИБ, тесты) + `bsl-analyzer` для CI.
- **Работа внутри IDE:** `EDT-MCP` + `CodePilot1C` в EDT, либо `1C: Platform Tools MCP` + skills в VS Code / Cursor.
- **Работа с учётными данными:** `aprovodka` (OData) или ARQA (коммерческий).

---

[![Star History Chart](https://api.star-history.com/image?repos=Untru/1c-mcp&type=date&legend=top-left)](https://www.star-history.com/?repos=Untru%2F1c-mcp&type=date&legend=top-left)

Лицензия: [CC0](https://creativecommons.org/publicdomain/zero/1.0/)
