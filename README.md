# Arc-NOVA

A user interface engine for interpreting and displaying content from NOVA and GSS files.

# WARNING

This protocol is still in active development and may change at any time. Do not use it for production or real-world applications until an official release is published. An official release will be marked by a version ending in .01 or higher. Version numbers are determined by the date on which the version was finalized. As of this writing, the current version is 2025.05.10.00, which represents a pre-release finalized on August 10, 2025. Please note that this README is not yet complete—more widgets and content will be added as updates and modifications continue.

## Overview
The NOVA project acts as a renderer for M3L (Multi-Media Markup Language) and GSS (Global Style Sheets), built to provide a consistent UI experience across multiple applications. It defines the UI layout using M3L and applies styling through a GSS file. This engine is also integrated into ArcanaLayer, a decentralized, cloud-based blockchain platform, where it functions as the UI layer.

While NOVA is the first renderer created for M3L and GSS, it is not meant to be the only one. At present, Python is the main programming language used, and QT6 is the base for UI. However, the protocol remains adaptable and can be implemented with other UI frameworks—or even game engines if needed.

The M3L and GSS standards are maintained by me but are intended to stay open and evolve over time. Below is a list of keywords used in M3L, along with example syntax. Both M3L and GSS follow a TOML-inspired formatting style.

## Modes
M3L and GSS support different modes to adjust the UI for various input methods or contexts—such as moving from mouse & keyboard to a controller or a touchscreen. Each mode provides its own layout and interaction model. Supported modes include:

- **Application Mode:** Classic desktop-style windowed mode, with UI features such as title bar, minimize/maximize buttons, and menu bars. Best for desktops with mouse and keyboard.
- **Dashboard Mode:** Fullscreen view within the UI engine, with a fixed viewport (window scrolling disabled, but widget scrolling allowed). Ideal for dashboards and summaries, optimized for controller use. It simplifies inputs, reducing complex fields like text, and favors controller-friendly layouts.
- **Web Mode:** Mimics a traditional website with vertical-only scrolling. Static elements can be pinned while the rest scrolls. Great for document-style or information-heavy layouts.
- **Desktop Mode:** Optimized for wide screens, enabling horizontal scrolling. Supports static elements and parallax scrolling for depth and motion during scroll events.

## Elements
In NOVA, an Element defines a UI structure made of multiple widgets, designed to achieve a specific function. Below are the core supported elements in the M3L/GSS ecosystem:

## Video Element
Embeds video into the UI, usually including:

- Reactions
- Goal bar
- Voting
- Quizzes
- Comments/Chat (for live sessions)
- Pop-ups (tooltip-style overlays)
- Closed Captioning (manual for now, AI-based planned)
- Ratings (audience targeting)
- Video suggestions

Missing fields in M3L should be gracefully handled by GSS.

## Video Catalog
Lets users browse and explore multiple videos, similar to an item selector without checkout.

## Map
Displays a 2D map or annotated image with interactive landmarks. Features:

- Custom markers
- Reactions/links per marker
- Suitable for static point-of-interest maps

## Background Audio
Plays ambient audio without direct user control except mute (via settings). Controlled via GSS. Automatically mutes when other media plays, though this can be customized.

## Spreadsheet
Manages structured tabular data with:

- Table widgets
- Tab widget
- Scroll widget
- Graph widget
- Special text areas

## Social Media
Replicates a feed layout, containing:

- Messaging widget
- Reaction widget
- Rating widget
- Mute widget

## Text Editor
A code editor-like environment, including:

- Line numbers
- Syntax-aware text area
- File explorer
- Status bar
- Search widget

## Word Processor
Similar to Text Editor but for writing. Adds spellcheck, formatting tools, and replaces line numbers with text formatting options.

## GSS Emulator
Used for theme previewing under different GSS styles for testing. Not intended for creating inconsistent themes.

## Markdown
Renders `.md` files into styled, readable UI views.

## Tiles
Displays a grid of card/poster widgets. Can include filters for search/sorting.

## Notification (Toast)
Temporary alerts. Types:

- Info
- Warning
- Error

## Gallery
Displays many images with optional titles and subtitles.

## Menu Bar
Top navigation container, includes:

- Icons and buttons
- Sliders, dropdowns, dividers
- Tabs and fullscreen slides

Note: One menu bar per application.

## Image Editor
Basic image editing with:

- Canvas
- Viewer
- Color picker
- Layer manager

## Node Graph
Visualizes relationships or ideas. Includes:

- Grid widget
- Shapes, arrows
- Color picker

Uses Obsidian’s open file format for node data.

## Card Section
Stylized 3-card layout on a unique background. Often used in web apps.

## Hero Section
A promotional UI block, usually for web. Includes:

- Header/sub-header (max 256 chars)
- Call-to-action button
- Optional image/icon and secondary action

## Article
For long-form content. Contains:

- Header widget
- Section headers
- Paragraphs

Could later evolve into a Book Element with chapters.

## Graph
Provides data visualizations:

- Types: line, bar, pie, scatter, candle
- Components: canvas, legend, header, checkboxes, hover bubbles

## Documentation
Like Article, but adds:

- Hyperlinks
- Table of contents
- Embedded media

# Built With

-Python 3.11.3

-Kivy

## Custom
User-defined element. Requires:

- Widget declarations
- Resizing rules
- State logic (undo/redo, revisions)

Note: Intended for special use cases, not for bypassing UI standards.
