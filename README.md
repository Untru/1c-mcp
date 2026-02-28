# Awesome 1C MCP Servers

Каталог MCP-серверов (Model Context Protocol) для экосистемы 1С:Предприятие.

MCP позволяет AI-ассистентам (Claude, Cursor, VS Code Copilot и др.) взаимодействовать с 1С: читать метаданные, запускать тесты, анализировать код, управлять базами и многое другое.

---

## Содержание

- [IDE-интеграции](#ide-интеграции)
- [Фреймворки для создания MCP-серверов](#фреймворки-для-создания-mcp-серверов)
- [Метаданные и анализ кода](#метаданные-и-анализ-кода)
- [Справка и документация платформы](#справка-и-документация-платформы)
- [Тестирование и проверка синтаксиса](#тестирование-и-проверка-синтаксиса)
- [Интеграция с 1С:Напарник](#интеграция-с-1снапарник)
- [Интеграция с учётными системами](#интеграция-с-учётными-системами)
- [Графовый анализ](#графовый-анализ)
- [Инфраструктура и DevOps](#инфраструктура-и-devops)
- [Оркестрация](#оркестрация)
- [Наборы правил и скиллов](#наборы-правил-и-скиллов)
- [Коммерческие продукты](#коммерческие-продукты)

---

## IDE-интеграции

### [EDT-MCP](https://github.com/DitriXNew/EDT-MCP)

MCP-сервер в виде плагина для 1C:EDT, обеспечивающий глубокую интеграцию AI-ассистентов с рабочим пространством IDE.

| | |
|---|---|
| **Язык** | Java |
| **Транспорт** | Streamable HTTP, SSE |
| **Требования** | EDT 2025.2.0+ |

**Возможности:**
- Навигация по проектам, модулям и метаданным конфигурации
- Анализ BSL-кода: структура модулей, поиск, иерархия вызовов
- Content Assist — подсказки типов, методов, документация платформы
- Валидация запросов 1С (синтаксис + семантика, режим СКД)
- Скриншоты форм из WYSIWYG-редактора
- Управление приложениями: обновление БД, запуск в режиме отладки
- Диагностика: ошибки, предупреждения, закладки, TODO/FIXME

---

## Фреймворки для создания MCP-серверов

### [1c_mcp](https://github.com/vladimir-kharin/1c_mcp)

Фреймворк для создания MCP-серверов внутри 1С:Предприятие через расширения конфигурации. Готовое расширение берёт на себя всю механику протокола — разработчику достаточно реализовать бизнес-логику инструментов.

| | |
|---|---|
| **Язык** | 1C Enterprise, Python (прокси) |
| **Транспорт** | HTTP (прямой), stdio (через Python-прокси) |
| **Требования** | 1С:Предприятие 8.3+ |

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

**Возможности:**
- HTTP-сервер запускается прямо внутри обработки 1С — Python не нужен
- Не требует изменений конфигурации и публикации на веб-сервере
- Не использует COM-соединение
- Выполнение запросов, получение метаданных
- Docker-деплой в режиме прокси

---

## Метаданные и анализ кода

### [1C_MCP_metadata](https://github.com/artesk/1C_MCP_metadata)

MCP-сервер для получения метаданных конфигурации 1С. Расширение 1С с HTTP-сервисом + PowerShell-мост для stdio.

| | |
|---|---|
| **Язык** | 1C Enterprise, PowerShell |
| **Транспорт** | stdio (через PowerShell) |
| **Требования** | 1С:Предприятие 8.3+ |

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

**Возможности:**
- Граф метаданных: объекты, модули, процедуры, формы, элементы, подписки
- Загрузка сигнатур процедур/функций, построение графа вызовов
- Полнотекстовый и гибридный поиск по описаниям процедур
- Мультипроектная поддержка
- Три режима поиска: LLM-агент (natural language → Cypher), шаблонный, гибридный

### [mcp-1c-v1](https://github.com/FSerg/mcp-1c-v1)

MCP-сервер с RAG (Retrieval-Augmented Generation) для описания структуры конфигурации 1С. Семантический поиск через векторную БД Qdrant.

| | |
|---|---|
| **Язык** | TypeScript |
| **Транспорт** | Streamable HTTP |
| **Требования** | Docker (Qdrant + Embedding Service) |

**Возможности:**
- Мульти-векторный поиск с RRF (Reciprocal Rank Fusion)
- Обработка 1С для экспорта структуры конфигурации
- Web UI (Streamlit) для загрузки данных в Qdrant
- MCP Inspector для отладки
- Docker Compose: Qdrant + Embedding + Loader + MCP Server

---

## Справка и документация платформы

### [mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)

MCP-сервер — интерактивный «Синтакс-помощник» для AI. Справка по синтаксису и объектной модели платформы 1С:Предприятие.

| | |
|---|---|
| **Язык** | Kotlin |
| **Транспорт** | stdio, SSE |
| **Требования** | JDK 17+, 1С:Предприятие 8.3.20+ |

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

**Возможности:**
- Навигация по определениям и ссылкам
- Диагностика кода (100+ проверок BSL LS)
- Hover-подсказки и рефакторинг
- Универсальный LSP→MCP мост (см. также [Tritlo/lsp-mcp](https://github.com/Tritlo/lsp-mcp) — generic вариант)

### [mcp-onec-test-runner (METR)](https://github.com/alkoleft/mcp-onec-test-runner)

MCP-сервер для запуска YaXUnit-тестов и сборки проектов 1С из AI-ассистентов.

| | |
|---|---|
| **Язык** | Kotlin |
| **Транспорт** | stdio |
| **Требования** | JDK 17+, 1С:Предприятие 8.3.10+, YaXUnit |

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

**Возможности:**
- `ask_1c_ai` — запросы к AI-ассистенту 1С
- `explain_1c_syntax` — объяснение элементов синтаксиса
- `check_1c_code` — анализ кода на ошибки
- Swagger UI для интерактивной документации
- Docker-деплой с multi-stage сборкой

---

## Интеграция с учётными системами

### [ARQA MCP Server](https://arqa.cc/ru/mcp-server)

Коммерческий on-premise MCP-сервер для интеграции AI-моделей с учётными системами 1С. Поддерживает работу с документами, отчётами и данными.

| | |
|---|---|
| **Язык** | Node.js |
| **Транспорт** | HTTP |
| **Требования** | Node.js 18+, 1С:Предприятие 8.3.18+ |

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

---

## Графовый анализ

### [bsl-graph](https://github.com/alkoleft/bsl-graph)

Анализатор и визуализатор конфигураций 1С. Строит граф знаний в NebulaGraph с MCP-доступом.

| | |
|---|---|
| **Язык** | Kotlin |
| **Транспорт** | MCP, REST API |
| **Требования** | JDK 17, NebulaGraph |

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

**Возможности:**
- Изолированная среда: AI не может повредить продуктивные данные
- Полноценное 1С-окружение: клиент, сервер, веб, БД
- Быстрое создание и удаление песочниц

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

| Проект | Stars | Категория |
|--------|-------|-----------|
| [1c_mcp](https://github.com/vladimir-kharin/1c_mcp) | ![Stars](https://img.shields.io/github/stars/vladimir-kharin/1c_mcp?style=flat&label=) | Фреймворк |
| [cursor_rules_1c](https://github.com/comol/cursor_rules_1c) | ![Stars](https://img.shields.io/github/stars/comol/cursor_rules_1c?style=flat&label=) | Правила и скиллы |
| [mcp-1c-v1](https://github.com/FSerg/mcp-1c-v1) | ![Stars](https://img.shields.io/github/stars/FSerg/mcp-1c-v1?style=flat&label=) | RAG / метаданные |
| [mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context) | ![Stars](https://img.shields.io/github/stars/alkoleft/mcp-bsl-platform-context?style=flat&label=) | Справка платформы |
| [EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | ![Stars](https://img.shields.io/github/stars/DitriXNew/EDT-MCP?style=flat&label=) | IDE |
| [mcp-onec-test-runner](https://github.com/alkoleft/mcp-onec-test-runner) | ![Stars](https://img.shields.io/github/stars/alkoleft/mcp-onec-test-runner?style=flat&label=) | Тестирование |
| [1c-mcp-toolkit](https://github.com/ROCTUP/1c-mcp-toolkit) | ![Stars](https://img.shields.io/github/stars/ROCTUP/1c-mcp-toolkit?style=flat&label=) | Фреймворк |
| [1C_MCP_metadata](https://github.com/artesk/1C_MCP_metadata) | ![Stars](https://img.shields.io/github/stars/artesk/1C_MCP_metadata?style=flat&label=) | Метаданные |
| [1c-mcp-metacode](https://github.com/ROCTUP/1c-mcp-metacode) | ![Stars](https://img.shields.io/github/stars/ROCTUP/1c-mcp-metacode?style=flat&label=) | Граф кода |
| [1c-syntax-helper-mcp](https://github.com/Antonio1C/1c-syntax-helper-mcp) | ![Stars](https://img.shields.io/github/stars/Antonio1C/1c-syntax-helper-mcp?style=flat&label=) | Документация |
| [1c-buddy](https://github.com/ROCTUP/1c-buddy) | ![Stars](https://img.shields.io/github/stars/ROCTUP/1c-buddy?style=flat&label=) | 1С:Напарник |
| [bsl-graph](https://github.com/alkoleft/bsl-graph) | ![Stars](https://img.shields.io/github/stars/alkoleft/bsl-graph?style=flat&label=) | Графовый анализ |
| [spring-mcp-1c-copilot](https://github.com/SteelMorgan/spring-mcp-1c-copilot) | ![Stars](https://img.shields.io/github/stars/SteelMorgan/spring-mcp-1c-copilot?style=flat&label=) | 1С:Напарник |
| [compose4mcp](https://github.com/pravets/compose4mcp) | ![Stars](https://img.shields.io/github/stars/pravets/compose4mcp?style=flat&label=) | Оркестрация |
| [1c-ai-sandbox](https://github.com/SteelMorgan/1c-ai-sandbox-client-server) | ![Stars](https://img.shields.io/github/stars/SteelMorgan/1c-ai-sandbox-client-server?style=flat&label=) | Песочница |
| [onec-help-mcp](https://github.com/rzateev/onec-help-mcp) | ![Stars](https://img.shields.io/github/stars/rzateev/onec-help-mcp?style=flat&label=) | Справка (RAG) |
| [mcp-bsl-lsp-bridge](https://github.com/SteelMorgan/mcp-bsl-lsp-bridge) | ![Stars](https://img.shields.io/github/stars/SteelMorgan/mcp-bsl-lsp-bridge?style=flat&label=) | BSL LS мост |
| [bsl-mcp](https://github.com/phsin/mcp-bsl-ls) | ![Stars](https://img.shields.io/github/stars/phsin/mcp-bsl-ls?style=flat&label=) | Линтер BSL |
| [1c-log-checker](https://github.com/SteelMorgan/1c-log-checker) | ![Stars](https://img.shields.io/github/stars/SteelMorgan/1c-log-checker?style=flat&label=) | Логи ЖР/ТЖ |
| [1c-accounting-mcp](https://github.com/tarasov46/1c-accounting-mcp) | ![Stars](https://img.shields.io/github/stars/tarasov46/1c-accounting-mcp?style=flat&label=) | Бухгалтерия |

### Коммерческие

| Проект | Категория | Цена |
|--------|-----------|------|
| [OneMCP](https://onemcp.ru) | SaaS-платформа | Бета (free) |
| [ARQA MCP Server](https://arqa.cc/ru/mcp-server) | Бизнес-операции | Paid |
| [OneRPA Suite](https://docs.onerpa.ru/mcp-servery-1c) | Набор серверов | Paid |
| [VibeCoding1C](http://vibecoding1c.ru) | Конструктор | Paid |
| [Infostart MCP](https://infostart.ru) | Метаданные | Paid |

---

## Как добавить проект

Нашли MCP-сервер для 1С, которого нет в списке? Откройте Issue или Pull Request.

---

## Лицензия

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
