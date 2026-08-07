# Awesome 1C MCP Servers

[![Check Links](https://github.com/Untru/1c-mcp/actions/workflows/links.yml/badge.svg)](https://github.com/Untru/1c-mcp/actions/workflows/links.yml)

Каталог MCP-серверов (Model Context Protocol) для экосистемы 1С:Предприятие.

MCP позволяет AI-ассистентам (Claude, Cursor, VS Code Copilot и др.) взаимодействовать с 1С: читать метаданные, запускать тесты, анализировать код, управлять базами и многое другое.

> **Хотите добавить проект?** Смотрите [CONTRIBUTING.md](CONTRIBUTING.md) | [Открыть Issue](.github/ISSUE_TEMPLATE/new-server.yml) | [Changelog](CHANGELOG.md)

---

## Содержание

- [Быстрая навигация](#быстрая-навигация)
- [Сценарии использования](#сценарии-использования)
- [Архитектурные паттерны](#архитектурные-паттерны)
- [Матрица совместимости](#матрица-совместимости)
- [IDE-интеграции](#ide-интеграции)
- [Фреймворки для создания MCP-серверов](#фреймворки-для-создания-mcp-серверов)
- [Метаданные и анализ кода](#метаданные-и-анализ-кода)
- [Справка и документация платформы](#справка-и-документация-платформы)
- [Тестирование и проверка синтаксиса](#тестирование-и-проверка-синтаксиса)
- [Интеграция с 1С:Напарник](#интеграция-с-1снапарник)
- [Интеграция с учётными системами](#интеграция-с-учётными-системами)
- [Графовый анализ](#графовый-анализ)
- [Инфраструктура и DevOps](#инфраструктура-и-devops)
- [Наборы правил и скиллов](#наборы-правил-и-скиллов)
- [Коммерческие продукты](#коммерческие-продукты)

---

## Star History

[![Star History Chart](https://api.star-history.com/image?repos=Untru/1c-mcp&type=date&legend=top-left)](https://www.star-history.com/?repos=Untru%2F1c-mcp&type=date&legend=top-left)

---

## Быстрая навигация

| Нужно | С чего начать |
|------|---------------|
| Работать из 1C:EDT | [EDT-MCP](#edt-mcp), [CodePilot1C](#codepilot1c) |
| Работать из VS Code / Cursor с проектом 1С | [1C: Platform Tools MCP](#1c-platform-tools-mcp), [Наборы правил и скиллов](#наборы-правил-и-скиллов) |
| Быстро подключить живую базу 1С | [mcp-1c](#mcp-1c), [1c_mcp](#1c_mcp), [1c-mcp-toolkit](#1c-mcp-toolkit) |
| Создать свой MCP-сервер внутри 1С | [1c_mcp](#1c_mcp), [http1c](#http1c), [1c-mcp-toolkit](#1c-mcp-toolkit) |
| Искать по метаданным и коду | [rlm-tools-bsl](#rlm-tools-bsl), [1c-mcp-metacode](#1c-mcp-metacode), [mcp-1c-v1](#mcp-1c-v1), [bsl-graph](#bsl-graph) |
| Получить справку по платформе и BSL | [mcp-bsl-platform-context](#mcp-bsl-platform-context), [onec-help-mcp](#onec-help-mcp), [1c-syntax-helper-mcp](#1c-syntax-helper-mcp) |
| Проверять BSL и запускать тесты | [bsl-analyzer](#bsl-analyzer), [bsl-mcp](#bsl-mcp), [mcp-bsl-lsp-bridge](#mcp-bsl-lsp-bridge), [mcp-onec-test-runner](#mcp-onec-test-runner-metr), [v8-runner](#v8-runner) |
| Искать готовые шаблоны кода | [1c-templates-mcp](#1c-templates-mcp), [compose4mcp](#compose4mcp) |
| Подключить учётные данные, каталоги и документы | [1c-rest-mcp](#1c-rest-mcp), [1c-accounting-mcp](#1c-accounting-mcp), [ARQA MCP Server](#arqa-mcp-server) |
| Вызывать внешние API и сервисы через 1С/OneScript | [OpenIntegrations](#openintegrations) |
| Агрегировать несколько клиентских сессий 1С | [v8-session-manager](#v8-session-manager) |
| Подключить Codex и Claude к 1С-разработке через plugin и skills | [Unica](#unica), [cursor_rules_1c](#cursor_rules_1c), [1C: Platform Tools Skills](#1c-platform-tools-skills) |

---

## Сценарии использования

Готовые ориентиры под конкретные задачи. Это не обязательные наборы «всё сразу», а типовые связки, с которых удобно начинать.

### AI пишет код обработки или расширения

> Агент получает контекст из метаданных и справки, пишет BSL-код, проверяет синтаксис и запускает тесты.

```
mcp-1c / 1c_mcp          — контекст живой базы и метаданные
  ↓
mcp-bsl-platform-context  — справка по платформенным типам
  ↓
bsl-analyzer             — диагностика BSL и отчёты
  ↓
mcp-onec-test-runner (METR)  — запуск YaXUnit-тестов
```

### AI разбирает большую конфигурацию

> Нужно быстро понять подсистему, механизм или доработку без долгой подготовки RAG-индекса.

```
rlm-tools-bsl / 1c-mcp-metacode  — точечное чтение BSL, метаданных и графа связей
  +
onec-help-mcp            — справка платформы и пояснение API
```

### AI делает code review BSL

> Агент анализирует код на ошибки, антипаттерны и несоответствие стандартам.

```
bsl-analyzer / mcp-bsl-lsp-bridge — диагностика, отчёты, LSP и навигация
  +
rlm-tools-bsl / 1c-mcp-metacode   — точечный поиск, метаданные и граф вызовов
  +
1c-buddy                         — проверка через 1С:Напарник
```

### AI помогает в локальном цикле разработки

> Агент собирает проект, готовит ИБ, запускает синтаксические проверки и тесты через управляемую поверхность.

```
v8-runner / mcp-onec-test-runner  — сборка, синтаксические проверки и тесты
  +
bsl-analyzer              — статический анализ и отчёты для CI
```

### AI работает с учётной системой

> Создание документов, поиск контрагентов, генерация отчётов через естественный язык.

```
1c-rest-mcp              — OData-операции (каталоги, документы)
  или
ARQA MCP Server          — бизнес-операции (коммерческий)
  +
onec-help-mcp            — справка для понимания доменной модели
```

### AI работает внутри IDE

> Работа в EDT, VS Code или Cursor: навигация, написание кода, команды IDE и проверка проекта.

```
EDT-MCP                   — навигация, BSL AST, формы и диагностика EDT
  +
CodePilot1C               — чат, агентный режим и QA-команды внутри EDT
  +
1C: Platform Tools MCP    — команды VS Code-расширения через MCP
  +
mcp-bsl-platform-context  — справка по API
  +
bsl-analyzer              — LSP и диагностика BSL
```

---

## Архитектурные паттерны

### Прямое подключение к базе

Расширение конфигурации + HTTP-сервис в 1С, MCP-сервер подключается напрямую.

**Когда:** нужен доступ к живым данным и метаданным, есть контроль над базой.

**Серверы:** `mcp-1c`, `1c_mcp`, `1c-mcp-toolkit`

### Работа с выгрузкой конфигурации

Парсинг XML/EDT-выгрузки без подключения к работающей базе.

**Когда:** CI/CD, code review, анализ без доступа к серверу 1С.

**Серверы:** `1c-mcp-metacode`, `bsl-graph`, `mcp-1c` (режим выгрузки)

### RAG / семантический поиск

Индексация метаданных и документации в векторной/графовой БД.

**Когда:** нужен поиск на естественном языке, большие конфигурации (ERP, БСП).

**Серверы:** `mcp-1c-v1` (Qdrant), `1c-mcp-metacode` (Neo4j), `onec-help-mcp`

### Мост к существующим инструментам

MCP-обёртка над LSP, REST API или другим протоколом.

**Когда:** уже есть инфраструктура (BSL LS, OData, 1С:Напарник), нужно дать к ней MCP-доступ.

**Серверы:** `mcp-bsl-lsp-bridge`, `1c-rest-mcp`, `1c-buddy`, `spring-mcp-1c-copilot`

---

## Матрица совместимости

### По транспорту

| Транспорт | Серверы |
|-----------|---------|
| stdio | mcp-1c, 1c-mcp-metacode, rlm-tools-bsl, bsl-analyzer, bsl-mcp, mcp-onec-test-runner, v8-runner, mcp-bsl-platform-context, 1C_MCP_metadata, 1c-rest-mcp, 1c-accounting-mcp, OpenIntegrations |
| SSE | EDT-MCP, mcp-bsl-platform-context, 1c-templates-mcp, spring-mcp-1c-copilot, http1c |
| Streamable HTTP | EDT-MCP, mcp-1c-v1, rlm-tools-bsl, 1c-rest-mcp, http1c, v8-runner, v8-session-manager |
| HTTP (generic или legacy) | 1c_mcp, 1c-mcp-toolkit, CodePilot1C, 1c-syntax-helper-mcp, ARQA MCP Server |

### По платформе 1С

| Версия 1С | Серверы |
|-----------|---------|
| 8.2.13+ | 1c-mcp-toolkit |
| 8.3.10+ | mcp-onec-test-runner |
| 8.3.18+ | ARQA MCP Server |
| 8.3.20+ | mcp-bsl-platform-context |
| 8.3.27.x | Unica (для операций, которым требуется запуск 1С) |
| 8.3+ (общее) | mcp-1c, 1c_mcp, 1C_MCP_metadata, v8-runner |
| Не требуется | 1c-mcp-metacode, rlm-tools-bsl, mcp-1c-v1, bsl-analyzer (CLI, LSP и offline MCP), bsl-mcp, mcp-bsl-lsp-bridge, 1c-rest-mcp, bsl-graph, onec-help-mcp |

### По зависимостям

| Зависимость | Серверы |
|-------------|---------|
| Docker | mcp-1c-v1, onec-help-mcp, 1c-syntax-helper-mcp, 1c-buddy, compose4mcp, 1c-ai-sandbox, OneRPA Suite |
| JDK 17+ | EDT-MCP, CodePilot1C, mcp-bsl-platform-context, mcp-onec-test-runner, bsl-graph |
| Neo4j | 1c-mcp-metacode |
| Qdrant | mcp-1c-v1, onec-help-mcp |
| BSL Language Server | bsl-mcp, mcp-bsl-lsp-bridge |
| Node.js | 1c-rest-mcp, ARQA MCP Server |
| OneScript 2.0+ | OpenIntegrations |
| Python | 1c_mcp (прокси), 1c-mcp-toolkit (прокси), 1c-mcp-metacode, rlm-tools-bsl, bsl-mcp, 1c-templates-mcp, onec-help-mcp |
| Rust | bsl-analyzer, v8-runner, v8-session-manager |

---

## IDE-интеграции

### [EDT-MCP](https://github.com/DitriXNew/EDT-MCP)

MCP-сервер в виде плагина для 1C:EDT, обеспечивающий глубокую интеграцию AI-ассистентов с рабочим пространством IDE.

| | |
|---|---|
| **Язык** | Java |
| **Транспорт** | Streamable HTTP, SSE |
| **Требования** | EDT 2025.2.0+ |
| **Статус** | ✅ Active |

**Возможности:**
- Навигация по проектам, модулям и метаданным конфигурации
- Анализ BSL-кода: структура модулей, поиск, иерархия вызовов
- Content Assist — подсказки типов, методов, документация платформы
- Валидация запросов 1С (синтаксис + семантика, режим СКД)
- Скриншоты форм из WYSIWYG-редактора
- Управление приложениями: обновление БД, запуск в режиме отладки
- Диагностика: ошибки, предупреждения, закладки, TODO/FIXME

### [CodePilot1C](https://github.com/ondysss/codepilot1c-edt)

AI-плагин для 1C:EDT с чатом, агентным режимом и MCP Host. Добавлен по открытому issue [Untru/1c-mcp#1](https://github.com/Untru/1c-mcp/issues/1).

| | |
|---|---|
| **Язык** | Java |
| **Транспорт** | MCP Host, HTTP |
| **Требования** | 1C:EDT, JDK 17 для сборки |
| **Статус** | ✅ Active |

**Возможности:**
- Чат и агентный режим внутри 1C:EDT
- Работа с BSL AST, метаданными и формами
- Диагностика проекта и QA-команды через MCP
- Подключение собственной модели
- Update site для установки в EDT

### [1C: Platform Tools MCP](https://github.com/yellow-hammer/mcp-1c-platform-tools)

MCP-сервер для вызова команд VS Code-расширения [1C: Platform Tools](https://marketplace.visualstudio.com/items?itemName=yellow-hammer.1c-platform-tools) из Cursor, VS Code и других MCP-клиентов.

| | |
|---|---|
| **Язык** | TypeScript |
| **Транспорт** | stdio, IPC к VS Code-расширению |
| **Требования** | VS Code/Cursor, расширение 1C: Platform Tools, включённый IPC |
| **Статус** | ✅ Active |

**Возможности:**
- Вызов команд расширения 1C: Platform Tools через MCP
- Работа с проектами 1С в формате `packagedef`
- Автоматическая регистрация MCP в VS Code
- Ручная настройка для Cursor через `.cursor/mcp.json`
- Связка с installable skills для агентов

---

## Фреймворки для создания MCP-серверов

### [1c_mcp](https://github.com/vladimir-kharin/1c_mcp)

Фреймворк для создания MCP-серверов внутри 1С:Предприятие через расширения конфигурации. Готовое расширение берёт на себя всю механику протокола — разработчику достаточно реализовать бизнес-логику инструментов.

| | |
|---|---|
| **Язык** | 1C Enterprise, Python (прокси) |
| **Транспорт** | HTTP (прямой), stdio (через Python-прокси) |
| **Требования** | 1С:Предприятие 8.3+ |
| **Статус** | ✅ Active |

**Возможности:**
- Готовое расширение `MCP_Сервер.cfe` — достаточно реализовать `ДобавитьИнструменты()` и `ВыполнитьИнструмент()`
- Встроенные инструменты для метаданных конфигурации
- Три режима подключения: прямой HTTP, через Python-прокси (stdio + OAuth2), Docker
- Поддержка Resources и Prompts (не только Tools)

### [1c-mcp-toolkit](https://github.com/ROCTUP/1c-mcp-toolkit)

MCP и REST API сервер для получения метаданных и данных из базы 1С. Уникальная особенность — встроенный HTTP-сервер прямо в обработке `.epf`.

| | |
|---|---|
| **Язык** | 1C Enterprise, Python (FastAPI) |
| **Транспорт** | HTTP (встроенный в .epf), HTTP long polling (прокси) |
| **Требования** | 1С:Предприятие 8.2.13+ / 8.3.25 |
| **Статус** | ✅ Active |

**Возможности:**
- HTTP-сервер запускается прямо внутри обработки 1С — Python не нужен
- Не требует изменений конфигурации и публикации на веб-сервере
- Не использует COM-соединение
- Выполнение запросов, произвольного кода, получение метаданных, журнала регистрации и объектов по ссылке
- REST API с теми же операциями для агентов без MCP
- Анонимизация чувствительных данных и изоляция каналов
- Готовые skills: `calling-1c-rest-api-via-curl`, `composing-1c-queries`
- Docker-деплой в режиме прокси

### [http1c](https://mcpmarket.com/server/http1c)

Фреймворк для публикации бизнес-логики 1С как MCP-сервера. Состоит из нативной DLL для транспортного слоя и шаблона обработки 1С для реализации Tools, Resources и Prompts.

| | |
|---|---|
| **Язык** | 1C Enterprise, C/C++ |
| **Транспорт** | Streamable HTTP, SSE |
| **Требования** | 1С:Предприятие, нативная компонента |
| **Статус** | ✅ Active |

**Возможности:**
- Динамическая регистрация tools, resources и prompts из 1С
- Bearer-аутентификация, проверка origin и rate limiting
- Progress streaming и курсорная пагинация
- Поддержка полного MCP-протокола для прикладной бизнес-логики

---

## Метаданные и анализ кода

### [mcp-1c](https://github.com/feenlace/mcp-1c)

MCP-сервер для работы с живой базой 1С:Предприятие. Один Go-бинарник без внешних runtime-зависимостей, подключается к HTTP-сервису 1С и может использовать выгрузку конфигурации для поиска по коду.

| | |
|---|---|
| **Язык** | Go, 1C Enterprise |
| **Транспорт** | stdio |
| **Требования** | HTTP-сервис 1С, опционально выгрузка конфигурации |
| **Статус** | ✅ Active |

**Возможности:**
- Чтение метаданных, форм и информации о конфигурации
- Выполнение запросов к данным с параметрами
- Поиск по BSL-коду: smart/BM25, regex, exact
- Чтение журнала регистрации
- Встроенная справка BSL и автоустановка расширения в базу

### [1C_MCP_metadata](https://github.com/artesk/1C_MCP_metadata)

MCP-сервер для получения метаданных конфигурации 1С. Расширение 1С с HTTP-сервисом + PowerShell-мост для stdio.

| | |
|---|---|
| **Язык** | 1C Enterprise, PowerShell |
| **Транспорт** | stdio (через PowerShell) |
| **Требования** | 1С:Предприятие 8.3+ |
| **Статус** | 🚧 Beta |

**Возможности:**
- Структура метаданных конфигурации с фильтрацией по типам объектов
- Детальная информация об объектах метаданных
- Поиск по имени, синониму и комментарию
- Валидация синтаксиса языка запросов 1С

### [1c-mcp-metacode](https://github.com/ROCTUP/1c-mcp-metacode)

Загружает метаданные и код конфигурации 1С в графовую БД Neo4j и предоставляет MCP-инструменты для поиска.

| | |
|---|---|
| **Язык** | Python, Cypher |
| **Транспорт** | stdio |
| **Требования** | Neo4j, экспорт конфигурации |
| **Статус** | ✅ Active |

**Возможности:**
- Граф метаданных: объекты, модули, процедуры, формы, элементы, подписки
- Загрузка сигнатур процедур/функций, построение графа вызовов
- Полнотекстовый и гибридный поиск по описаниям процедур
- Мультипроектная поддержка
- Три режима поиска: LLM-агент (natural language → Cypher), шаблонный, гибридный

### [rlm-tools-bsl](https://github.com/Dach-Coin/rlm-tools-bsl)

MCP-сервер для токен-эффективного анализа больших кодовых баз 1С без обязательного RAG. Адаптирует RLM-подход под BSL, исходники CF, EDT, CFE и MDO, XML-метаданные и кириллический код.

| | |
|---|---|
| **Язык** | Python, PowerShell, Shell, 1C Enterprise |
| **Транспорт** | Streamable HTTP (рекомендуется), stdio |
| **Требования** | Python 3.10+, PyPI или uv; опционально Docker, systemd или Windows-служба |
| **Статус** | ✅ Active |

**Возможности:**
- 6 MCP-инструментов и песочница с 62 хелперами для анализа BSL и метаданных
- SQLite-индекс методов и графа вызовов для больших конфигураций
- Поддержка CF, EDT, CFE, MDO, BSL-модулей и XML-описаний объектов
- Реестр проектов, сессионные кэши, таймауты и подтверждение мутирующих операций
- `git_search` через `git grep` для исходников, находящихся в Git-репозитории
- Опциональные `llm_query`-хелперы через OpenAI-compatible endpoint'ы или Anthropic API

### [mcp-1c-v1](https://github.com/FSerg/mcp-1c-v1)

MCP-сервер с RAG (Retrieval-Augmented Generation) для описания структуры конфигурации 1С. Семантический поиск через векторную БД Qdrant.

| | |
|---|---|
| **Язык** | TypeScript |
| **Транспорт** | Streamable HTTP |
| **Требования** | Docker (Qdrant + Embedding Service) |
| **Статус** | 🚧 Beta |

**Возможности:**
- Мульти-векторный поиск с RRF (Reciprocal Rank Fusion)
- Обработка 1С для экспорта структуры конфигурации
- Web UI (Streamlit) для загрузки данных в Qdrant
- MCP Inspector для отладки
- Docker Compose: Qdrant + Embedding + Loader + MCP Server

### [1c-templates-mcp](https://yellowmcp.com/servers/1c-templates-mcp)

MCP-сервер для семантического поиска по шаблонам BSL-кода. Полезен как отдельный источник готовых заготовок и как дополнение к серверам метаданных.

| | |
|---|---|
| **Язык** | Python |
| **Транспорт** | SSE |
| **Требования** | Docker, ChromaDB, embedding-модель |
| **Статус** | ✅ Active |

**Возможности:**
- 2200+ предустановленных шаблонов кода 1С
- Семантический и полнотекстовый поиск
- CRUD Web UI с Monaco Editor
- Поддержка OpenAI-compatible embeddings и локальных SentenceTransformers

---

## Справка и документация платформы

### [mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)

MCP-сервер — интерактивный «Синтакс-помощник» для AI. Справка по синтаксису и объектной модели платформы 1С:Предприятие.

| | |
|---|---|
| **Язык** | Kotlin |
| **Транспорт** | stdio, SSE |
| **Требования** | JDK 17+, 1С:Предприятие 8.3.20+ |
| **Статус** | ✅ Active |

**Возможности:**
- Нечёткий поиск по справке платформы (функции, методы, свойства, типы данных)
- Навигация по объектной модели — методы и свойства конкретных типов
- Информация о конструкторах платформенных объектов
- Spring Boot 3.5.0 + Spring AI + Kotlin Coroutines

### [onec-help-mcp](https://github.com/rzateev/onec-help-mcp)

MCP-сервер с RAG-поиском по официальной справке платформы 1С. Гибридный поиск (BM25 + семантика) с поддержкой нескольких версий платформы.

| | |
|---|---|
| **Язык** | Python 3.12+ |
| **Транспорт** | MCP, REST API |
| **Требования** | Docker (Qdrant + Embedding Service) |
| **Статус** | ✅ Active |

**Возможности:**
- Гибридный поиск: точное совпадение (BM25) + семантическое понимание
- Мультиверсионность платформы (8.3.24, 8.3.26 и др.)
- Структурированный API для поиска функций, методов, свойств и типов
- Двойной доступ: MCP для IDE + REST API для скриптов
- Docker-деплой с CPU/GPU режимами

### [1c-syntax-helper-mcp](https://github.com/Antonio1C/1c-syntax-helper-mcp)

MCP-сервер для быстрого поиска по документации синтаксиса 1С. Централизованный сервис для нескольких пользователей.

| | |
|---|---|
| **Язык** | Python (FastAPI) |
| **Транспорт** | HTTP |
| **Требования** | Docker (Elasticsearch), файл `.hbk` от платформы 1С |
| **Статус** | ✅ Active |

**Возможности:**
- Полнотекстовый поиск по `.hbk`-файлу документации платформы
- Elasticsearch-индексация
- Поддержка 8+ одновременных пользователей VS Code
- Мульти-архитектурные Docker-образы (AMD64, ARM64)

---

## Тестирование и проверка синтаксиса

### [bsl-mcp](https://github.com/phsin/mcp-bsl-ls)

MCP-сервер для анализа и форматирования кода 1С через BSL Language Server. Проверяет `.bsl` и `.os` файлы, возвращает ошибки и предупреждения в JSON.

| | |
|---|---|
| **Язык** | Python 3.10+ |
| **Транспорт** | stdio |
| **Требования** | JRE 8+, BSL Language Server JAR |
| **Статус** | ✅ Active |

**Возможности:**
- Анализ одиночных файлов и целых каталогов
- Форматирование кода
- Настраиваемые лимиты памяти JVM и конфигурация
- Вывод в human-readable и структурированном JSON форматах

### [mcp-bsl-lsp-bridge](https://github.com/SteelMorgan/mcp-bsl-lsp-bridge)

LSP → MCP транслятор: даёт AI-агентам доступ к возможностям BSL Language Server — навигация по коду, поиск символов, диагностика (100+ проверок), рефакторинг, hover-подсказки.

| | |
|---|---|
| **Язык** | — |
| **Транспорт** | MCP |
| **Требования** | BSL Language Server |
| **Статус** | 🚧 Beta |

**Возможности:**
- Навигация по определениям и ссылкам
- Диагностика кода (100+ проверок BSL LS)
- Hover-подсказки и рефакторинг
- Универсальный LSP→MCP мост (см. также [Tritlo/lsp-mcp](https://github.com/Tritlo/lsp-mcp) — generic вариант)

### [bsl-analyzer](https://github.com/itrous/bsl-analyzer)

Высокопроизводительный анализатор BSL на Rust с CLI, LSP и встроенным MCP-сервером. Даёт IDE и AI-агентам диагностику, навигацию, поиск по проекту и справке, а также машинно-читаемые отчёты для CI/CD.

| | |
|---|---|
| **Язык** | Rust, 1C Enterprise, Shell, Python |
| **Транспорт** | MCP (stdio или локальный broker), LSP |
| **Требования** | Бинарник bsl-analyzer; для live-инструментов — опубликованное расширение или HTTP-сервис 1С |
| **Статус** | 🚧 Beta |

**Возможности:**
- 180 диагностик качества BSL-кода
- LSP-сервер для VS Code, Cursor, VSCodium, Zed и других IDE
- MCP-профили `reference` и `workspace` для справки платформы и работы с проектом
- CLI-анализ проекта с выводом в консоль, SARIF и JSONL
- Конфигурация через `bsl-analyzer.toml`
- Кроссплатформенность: Linux, Windows, macOS (Apple Silicon)

### [mcp-onec-test-runner (METR)](https://github.com/alkoleft/mcp-onec-test-runner)

MCP-сервер для запуска YaXUnit-тестов и сборки проектов 1С из AI-ассистентов.

| | |
|---|---|
| **Язык** | Kotlin |
| **Транспорт** | stdio |
| **Требования** | JDK 17+, 1С:Предприятие 8.3.10+, YaXUnit |
| **Статус** | ✅ Active |

**Возможности:**
- Запуск всех тестов или тестов конкретного модуля
- Сборка проекта 1С
- Проверка синтаксиса через Конфигуратор и 1C:EDT
- Быстрая конвертация EDT через авто-запуск EDT CLI
- Поддержка форматов DESIGNER и EDT

---

## Интеграция с 1С:Напарник

### [1c-buddy](https://github.com/ROCTUP/1c-buddy)

Чат, MCP-сервер и OpenAI-совместимый API-шлюз для общения с 1С:Напарник. Веб-интерфейс с подсветкой BSL/XML, визуализацией диаграмм и историей разговоров.

| | |
|---|---|
| **Язык** | JavaScript, Python |
| **Транспорт** | MCP, OpenAI API (`/v1/chat/completions`) |
| **Требования** | Docker, токен code.1c.ai |
| **Статус** | ✅ Active |

**Возможности:**
- `ask_1c_ai` — общие вопросы по 1С:Предприятие
- `explain_1c_syntax` — объяснение объектов и синтаксиса с контекстом
- `check_1c_code` — проверка кода на ошибки (синтаксис, логика, производительность)
- Веб-чат с подсветкой BSL/XML, вложениями файлов, экспортом в JSON
- Потоковые и непотоковые ответы через OpenAI-совместимый API

### [spring-mcp-1c-copilot](https://github.com/SteelMorgan/spring-mcp-1c-copilot)

MCP-сервер на Spring Boot для интеграции с API 1С:Напарник. SSE-транспорт и Swagger UI.

| | |
|---|---|
| **Язык** | Kotlin |
| **Транспорт** | SSE, REST API |
| **Требования** | JDK 17+, токен 1С:Напарник, Docker (опц.) |
| **Статус** | 🚧 Beta |

**Возможности:**
- `ask_1c_ai` — запросы к AI-ассистенту 1С
- `explain_1c_syntax` — объяснение элементов синтаксиса
- `check_1c_code` — анализ кода на ошибки
- Swagger UI для интерактивной документации
- Docker-деплой с multi-stage сборкой

---

## Интеграция с учётными системами

### [1c-rest-mcp](https://github.com/theYahia/1c-rest-mcp)

MCP-сервер для работы с опубликованным REST API 1С:Предприятие. Ориентирован на базовые операции с каталогами и документами.

| | |
|---|---|
| **Язык** | TypeScript |
| **Транспорт** | stdio, Streamable HTTP |
| **Требования** | Node.js, опубликованный OData/REST API 1С, Basic Auth |
| **Статус** | ✅ Active |

**Возможности:**
- Подключение к 1С через стандартный REST API
- Работа с каталогами, документами, регистрами и отчётами
- 9 MCP-инструментов: чтение, создание и обновление документов, произвольные OData-запросы
- Skills-обёртки `skill-catalog` и `skill-documents`
- Конфигурируемый base URL и Basic Auth
- Запуск через `npx`

### [ARQA MCP Server](https://arqa.cc/ru/mcp-server)

Коммерческий on-premise MCP-сервер для интеграции AI-моделей с учётными системами 1С. Поддерживает работу с документами, отчётами и данными.

| | |
|---|---|
| **Язык** | Node.js |
| **Транспорт** | HTTP |
| **Требования** | Node.js 18+, 1С:Предприятие 8.3.18+ |
| **Статус** | ✅ Active |

**Возможности:**
- Создание документов (счета, акты, накладные) через AI
- Поиск контрагентов, документов, остатков
- Генерация отчётов (ОСВ, дебиторка, продажи) на естественном языке
- TLS-шифрование, ролевой доступ, аудит, IP-фильтрация
- Поддержка: Бухгалтерия 3.0, УТ 11, ERP 2.4/2.5, ЗУП 3.1

> Коммерческий продукт. 14 дней бесплатного доступа.

### [1c-accounting-mcp](https://github.com/tarasov46/1c-accounting-mcp)

MCP-сервер для интеграции AI-ассистентов с 1С:Бухгалтерией. Ранняя стадия разработки.

| | |
|---|---|
| **Язык** | Python, JavaScript |
| **Транспорт** | stdio (через npx) |
| **Требования** | Python 3.8+, Node.js 16+ |
| **Статус** | 🔬 Experimental |

### [OpenIntegrations](https://github.com/Bayselonarrend/OpenIntegrations)

Open-source пакет интеграций для 1С:Предприятие и OneScript со встроенным stdio MCP-сервером. Позволяет AI-агенту вызывать методы более чем 30 внешних сервисов и технологий через единый OInt CLI.

| | |
|---|---|
| **Язык** | OneScript, 1C Enterprise |
| **Транспорт** | stdio |
| **Требования** | OInt CLI; OneScript 2.0+ при запуске из исходников |
| **Статус** | ✅ Active |

**Возможности:**
- Обнаружение доступных сервисов, методов и параметров через MCP-инструменты
- Вызов методов Telegram, Bitrix24, Google, Yandex, СУБД и других интеграций
- Использование как библиотеки 1С/OneScript и как кроссплатформенного CLI
- Конфигурационные переменные для работы с секретами без передачи значений AI-агенту
- Готовые примеры подключения к Cursor, Kiro и Cline

---

## Графовый анализ

### [bsl-graph](https://github.com/alkoleft/bsl-graph)

Анализатор и визуализатор конфигураций 1С. Строит граф знаний в NebulaGraph с MCP-доступом.

| | |
|---|---|
| **Язык** | Kotlin |
| **Транспорт** | MCP, REST API |
| **Требования** | JDK 17, NebulaGraph |
| **Статус** | 🚧 Beta |

**Возможности:**
- Полный анализ метаданных через `bsl-mdclasses`
- Интерактивная веб-визуализация (Sigma.js)
- Поддержка экспорта Конфигуратора и формата EDT
- Spring Boot 3.5.0 / Kotlin 2.1.20

---

## Инфраструктура и DevOps

### [1c-log-checker](https://github.com/SteelMorgan/1c-log-checker)

MCP-сервер для работы с журналом регистрации (ЖР) и технологическим журналом (ТЖ) 1С. Парсинг логов через ClickHouse + Grafana, MCP-доступ для AI-агента.

| | |
|---|---|
| **Язык** | — |
| **Транспорт** | MCP |
| **Требования** | ClickHouse, Grafana, Docker |
| **Статус** | 🚧 Beta |

**Возможности:**
- Парсинг и хранение ЖР и ТЖ в ClickHouse
- Визуализация через Grafana
- MCP-инструменты для чтения, создания и конфигурирования ТЖ
- AI-агент анализирует логи и находит проблемы

### [1c-ai-sandbox-client-server](https://github.com/SteelMorgan/1c-ai-sandbox-client-server)

Docker-песочница для безопасной работы AI-агента с 1С. Полноценное окружение (клиент + сервер + веб-публикация + БД), изолированное от продуктивных данных.

| | |
|---|---|
| **Язык** | Docker |
| **Транспорт** | — |
| **Требования** | Docker |
| **Статус** | 🔬 Experimental |

**Возможности:**
- Изолированная среда: AI не может повредить продуктивные данные
- Полноценное 1С-окружение: клиент, сервер, веб, БД
- Быстрое создание и удаление песочниц

### [v8-runner](https://github.com/alkoleft/v8-runner-rust)

CLI и MCP-сервер на Rust для локального цикла разработки 1С. Один entrypoint собирает исходники, готовит информационную базу, запускает проверки и тесты, выгружает изменения обратно в файлы и отдаёт AI-агентам ограниченную MCP-поверхность.

| | |
|---|---|
| **Язык** | Rust, Shell, Python |
| **Транспорт** | stdio, Streamable HTTP |
| **Требования** | 1С:Предприятие, Designer или IBCMD для реальных операций; YaXUnit и Vanessa Automation опционально |
| **Статус** | 🚧 Beta |

**Возможности:**
- Единый `v8project.yaml` для исходников, рабочей ИБ, инструментов и тестов
- Поддержка наборов исходников `DESIGNER` и `EDT`
- Builder backend'ы `DESIGNER` и `IBCMD`
- Запуск syntax check, YaXUnit и Vanessa Automation
- Машиночитаемый вывод `--json-message` для CI и AI-агентов
- MCP-команды `mcp serve stdio` и `mcp serve http` с 8 инструментами автоматизации

### [compose4mcp](https://github.com/pravets/compose4mcp)

Коллекция Docker Compose конфигов для оркестрации MCP-серверов для 1С-разработки.

| | |
|---|---|
| **Язык** | Docker Compose |

**Включённые серверы:**
- `1c_code_metadata_mcp` — поиск по метаданным и коду
- `1c_help_mcp` — поиск по справке платформы
- `1c_syntaxcheck_mcp` — проверка синтаксиса BSL
- `1c-code-checker` — интеграция с 1С:Напарник
- `mcp_ssl_server` — поиск по БСП
- `template-search-mcp` — шаблоны кода

### [v8-session-manager](https://github.com/1c-neurofish/v8-session-manager)

Менеджер клиентских сессий 1С для связки 1С-клиентов и AI-агентов. Принимает WebSocket-подключения от 1С-клиентов, агрегирует опубликованные ими MCP-инструменты и отдаёт единый MCP HTTP endpoint.

| | |
|---|---|
| **Язык** | Rust |
| **Транспорт** | WebSocket для 1С-клиентов, Streamable HTTP MCP для AI-агентов |
| **Требования** | 1С-клиенты с MCP WS-режимом, например через [onec-client-mcp-devkit](https://github.com/1c-neurofish/onec-client-mcp-devkit) |
| **Статус** | 🚧 Beta |

**Возможности:**
- Один бинарник с двумя портами: WS `:4000/sessions` и MCP HTTP `:4001/mcp`
- Единый `tools/list` для нескольких активных клиентских сессий 1С
- Префиксы инструментов по сессиям: `<session_prefix>__<tool_name>`
- Встроенный инструмент `session_list`
- Per-session FIFO, soft-reconnect, idle cleanup и дедупликация tools

### OneRPA MCP Suite

Набор Docker-контейнеров MCP-серверов от [OneRPA](https://docs.onerpa.ru/mcp-servery-1c) для 1С-разработки.

| Сервер | Порт | Назначение |
|--------|------|-----------|
| HelpSearchServer | 8003 | Поиск по справке платформы 1С |
| CodeMetadataSearchServer | 8000 | Поиск по метаданным и коду конфигурации |
| CloudEmbeddingsServer | 8000 | Облачная индексация с параллельными эмбеддингами |
| Graph Metadata Search | 8006 | Графовый поиск связей метаданных |
| SSLSearchServer | 8008 | Поиск по БСП (Библиотеке стандартных подсистем) |
| SyntaxCheckServer | 8002 | Проверка синтаксиса BSL |
| TemplatesSearchServer | 8004 | Шаблоны кода 1С |
| FormsServer | 8011 | Схемы для генерации форм |
| 1CCodeChecker | 8007 | Интеграция с 1С:Напарник |

---

## Наборы правил и скиллов

### [Unica](https://github.com/IngvarConsulting/unica)

Плагин для Codex и Claude Code, который помогает работать с проектами 1С:Предприятие. Это не самостоятельный MCP-сервер общего назначения, а воспроизводимый набор skills, MCP-сервер `unica`, сценарии и pinned-инструменты для 1С-разработки.

| | |
|---|---|
| **Язык** | Rust, Python, Shell |
| **Формат** | Плагин для Codex и Claude, skills, MCP-сервер `unica`, `.mcp.json` |
| **Требования** | Codex CLI или Claude Code, Git; для операций с запуском 1С — платформа 1С 8.3.27.x |
| **Статус** | ✅ Active |

**Возможности:**
- Skills для форм, метаданных, EPF/ERF, баз, ролей, СКД, веб-публикации и других задач 1С
- Единый MCP runtime `unica` для создания и проверки объектов, запуска 1С и поиска BSL-кода
- Установка через marketplace в Codex и Claude Code
- Один каталог плагина для обоих хостов с соседними манифестами
- Загрузка runtime из релизов с SHA-256-проверкой архивов и файлов
- Поддержка Windows, Linux и macOS

### [cursor_rules_1c](https://github.com/comol/cursor_rules_1c)

Комплексный набор правил, агентов и скиллов для AI-разработки на платформе 1С в Cursor IDE. Не является MCP-сервером напрямую, но активно использует MCP-серверы из этого списка.

| | |
|---|---|
| **Язык** | 1C Enterprise 8.3, Markdown |

**Возможности:**
- 11 специализированных AI-агентов (разработчик, архитектор, код-ревьюер и др.)
- 24+ скиллов (формы, запросы, шаблоны, роли, интеграции)
- Каталог антипаттернов с уровнями критичности
- Интеграция с MCP-серверами: `docsearch`, `codesearch`, `syntaxcheck`, `ssl_search` и др.

### [1C: Platform Tools Skills](https://marketplace.visualstudio.com/items?itemName=yellow-hammer.1c-platform-tools)

Набор installable skills для агентов Cursor, GitHub Copilot и Claude, поставляемый вместе с расширением 1C: Platform Tools. Не является отдельным MCP-сервером, но помогает агенту правильно вызывать команды расширения и работать с проектами 1С.

| | |
|---|---|
| **Формат** | `SKILL.md` |
| **IDE** | Cursor, VS Code Copilot, Claude |
| **Требования** | 1C: Platform Tools |

**Возможности:**
- Установка в `.cursor/skills/`, `.github/copilot/skills/` или `.claude/skills/`
- Описание команд расширения для AI-агентов
- Запуск команд через файл-триггер `.cursor/1c-platform-tools-run-command`
- Совместная работа с [1C: Platform Tools MCP](#1c-platform-tools-mcp)

---

## Коммерческие продукты

### [OneMCP](https://onemcp.ru)

SaaS-платформа с MCP-сервером, семантическим поиском по метаданным, коду и документации. Командная работа до 100 человек.

| Тариф | Конфигурации | Хранение | Статус |
|-------|-------------|----------|--------|
| Free | 1 | 100 МБ | Бета (бесплатно) |
| Basic | 5 | 1 ГБ | Бета (бесплатно) |
| Pro | Расширенный | — | Бета (бесплатно) |

> На февраль 2026 все тарифы бесплатны (бета).

### [VibeCoding1C](http://vibecoding1c.ru)

Коммерческий конструктор MCP-серверов для 1С без программирования. Также предлагает обучающие курсы.

| Продукт | Стоимость |
|---------|-----------|
| Конструктор MCP-серверов | 9 000 руб. |
| Курс по MCP серверам | 8 000 руб. |
| Курс по вайбкодингу | 15 000 руб. |

### [Infostart MCP](https://infostart.ru)

MCP от Инфостарт для работы с метаданными конфигураций. Гибридный поиск (BM25), подключение к синтаксис-помощнику. Набор Docker-контейнеров для проверки синтаксиса, поиска по справке и метаданным.

---

## Сводная таблица

### Open Source

| Проект | Stars | Категория | Статус |
|--------|-------|-----------|--------|
| [mcp-1c](https://github.com/feenlace/mcp-1c) | ![Stars](https://img.shields.io/github/stars/feenlace/mcp-1c?style=flat&label=) | Живая база / метаданные | ✅ |
| [1c_mcp](https://github.com/vladimir-kharin/1c_mcp) | ![Stars](https://img.shields.io/github/stars/vladimir-kharin/1c_mcp?style=flat&label=) | Фреймворк | ✅ |
| [Unica](https://github.com/IngvarConsulting/unica) | ![Stars](https://img.shields.io/github/stars/IngvarConsulting/unica?style=flat&label=) | Плагин и скиллы для Codex и Claude | ✅ |
| [cursor_rules_1c](https://github.com/comol/cursor_rules_1c) | ![Stars](https://img.shields.io/github/stars/comol/cursor_rules_1c?style=flat&label=) | Правила и скиллы | ✅ |
| [CodePilot1C](https://github.com/ondysss/codepilot1c-edt) | ![Stars](https://img.shields.io/github/stars/ondysss/codepilot1c-edt?style=flat&label=) | IDE | ✅ |
| [1C: Platform Tools MCP](https://github.com/yellow-hammer/mcp-1c-platform-tools) | ![Stars](https://img.shields.io/github/stars/yellow-hammer/mcp-1c-platform-tools?style=flat&label=) | IDE | ✅ |
| [mcp-1c-v1](https://github.com/FSerg/mcp-1c-v1) | ![Stars](https://img.shields.io/github/stars/FSerg/mcp-1c-v1?style=flat&label=) | RAG / метаданные | 🚧 |
| [mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context) | ![Stars](https://img.shields.io/github/stars/alkoleft/mcp-bsl-platform-context?style=flat&label=) | Справка платформы | ✅ |
| [EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | ![Stars](https://img.shields.io/github/stars/DitriXNew/EDT-MCP?style=flat&label=) | IDE | ✅ |
| [mcp-onec-test-runner](https://github.com/alkoleft/mcp-onec-test-runner) | ![Stars](https://img.shields.io/github/stars/alkoleft/mcp-onec-test-runner?style=flat&label=) | Тестирование | ✅ |
| [1c-mcp-toolkit](https://github.com/ROCTUP/1c-mcp-toolkit) | ![Stars](https://img.shields.io/github/stars/ROCTUP/1c-mcp-toolkit?style=flat&label=) | Фреймворк | ✅ |
| [http1c](https://mcpmarket.com/server/http1c) | — | Фреймворк | ✅ |
| [1C_MCP_metadata](https://github.com/artesk/1C_MCP_metadata) | ![Stars](https://img.shields.io/github/stars/artesk/1C_MCP_metadata?style=flat&label=) | Метаданные | 🚧 |
| [1c-mcp-metacode](https://github.com/ROCTUP/1c-mcp-metacode) | ![Stars](https://img.shields.io/github/stars/ROCTUP/1c-mcp-metacode?style=flat&label=) | Граф кода | ✅ |
| [rlm-tools-bsl](https://github.com/Dach-Coin/rlm-tools-bsl) | ![Stars](https://img.shields.io/github/stars/Dach-Coin/rlm-tools-bsl?style=flat&label=) | RLM-анализ BSL | ✅ |
| [1c-templates-mcp](https://yellowmcp.com/servers/1c-templates-mcp) | — | Шаблоны BSL | ✅ |
| [1c-syntax-helper-mcp](https://github.com/Antonio1C/1c-syntax-helper-mcp) | ![Stars](https://img.shields.io/github/stars/Antonio1C/1c-syntax-helper-mcp?style=flat&label=) | Документация | ✅ |
| [1c-buddy](https://github.com/ROCTUP/1c-buddy) | ![Stars](https://img.shields.io/github/stars/ROCTUP/1c-buddy?style=flat&label=) | 1С:Напарник | ✅ |
| [bsl-graph](https://github.com/alkoleft/bsl-graph) | ![Stars](https://img.shields.io/github/stars/alkoleft/bsl-graph?style=flat&label=) | Графовый анализ | 🚧 |
| [spring-mcp-1c-copilot](https://github.com/SteelMorgan/spring-mcp-1c-copilot) | ![Stars](https://img.shields.io/github/stars/SteelMorgan/spring-mcp-1c-copilot?style=flat&label=) | 1С:Напарник | 🚧 |
| [compose4mcp](https://github.com/pravets/compose4mcp) | ![Stars](https://img.shields.io/github/stars/pravets/compose4mcp?style=flat&label=) | Оркестрация | ✅ |
| [v8-session-manager](https://github.com/1c-neurofish/v8-session-manager) | ![Stars](https://img.shields.io/github/stars/1c-neurofish/v8-session-manager?style=flat&label=) | Оркестрация сессий | 🚧 |
| [1c-ai-sandbox](https://github.com/SteelMorgan/1c-ai-sandbox-client-server) | ![Stars](https://img.shields.io/github/stars/SteelMorgan/1c-ai-sandbox-client-server?style=flat&label=) | Песочница | 🔬 |
| [onec-help-mcp](https://github.com/rzateev/onec-help-mcp) | ![Stars](https://img.shields.io/github/stars/rzateev/onec-help-mcp?style=flat&label=) | Справка (RAG) | ✅ |
| [bsl-analyzer](https://github.com/itrous/bsl-analyzer) | ![Stars](https://img.shields.io/github/stars/itrous/bsl-analyzer?style=flat&label=) | BSL-анализатор и LSP | 🚧 |
| [mcp-bsl-lsp-bridge](https://github.com/SteelMorgan/mcp-bsl-lsp-bridge) | ![Stars](https://img.shields.io/github/stars/SteelMorgan/mcp-bsl-lsp-bridge?style=flat&label=) | BSL LS мост | 🚧 |
| [bsl-mcp](https://github.com/phsin/mcp-bsl-ls) | ![Stars](https://img.shields.io/github/stars/phsin/mcp-bsl-ls?style=flat&label=) | Линтер BSL | ✅ |
| [v8-runner](https://github.com/alkoleft/v8-runner-rust) | ![Stars](https://img.shields.io/github/stars/alkoleft/v8-runner-rust?style=flat&label=) | Локальный workflow и DevOps | 🚧 |
| [1c-log-checker](https://github.com/SteelMorgan/1c-log-checker) | ![Stars](https://img.shields.io/github/stars/SteelMorgan/1c-log-checker?style=flat&label=) | Логи ЖР/ТЖ | 🚧 |
| [1c-rest-mcp](https://github.com/theYahia/1c-rest-mcp) | ![Stars](https://img.shields.io/github/stars/theYahia/1c-rest-mcp?style=flat&label=) | REST API | ✅ |
| [1c-accounting-mcp](https://github.com/tarasov46/1c-accounting-mcp) | ![Stars](https://img.shields.io/github/stars/tarasov46/1c-accounting-mcp?style=flat&label=) | Бухгалтерия | 🔬 |
| [OpenIntegrations](https://github.com/Bayselonarrend/OpenIntegrations) | ![Stars](https://img.shields.io/github/stars/Bayselonarrend/OpenIntegrations?style=flat&label=) | Внешние API / интеграции | ✅ |

### Коммерческие

| Проект | Категория | Цена |
|--------|-----------|------|
| [OneMCP](https://onemcp.ru) | SaaS-платформа | Бета (free) |
| [ARQA MCP Server](https://arqa.cc/ru/mcp-server) | Бизнес-операции | Paid |
| [OneRPA Suite](https://docs.onerpa.ru/mcp-servery-1c) | Набор серверов | Paid |
| [VibeCoding1C](http://vibecoding1c.ru) | Конструктор | Paid |
| [Infostart MCP](https://infostart.ru) | Метаданные | Paid |

---

## Легенда статусов

| Статус | Значение |
|--------|----------|
| ✅ Active | Активная разработка, стабильная версия |
| 🚧 Beta | Работает, но API может измениться |
| 🔬 Experimental | Ранний прототип |
| 📦 Archived | Не поддерживается |

---

## Как добавить проект

Нашли MCP-сервер для 1С, которого нет в списке? Смотрите [CONTRIBUTING.md](CONTRIBUTING.md) — там шаблон записи и правила. Или просто откройте [Issue](https://github.com/Untru/1c-mcp/issues/new?template=new-server.yml).

---

## Лицензия

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
