# Excel-Assassin-w-Gemini
Excel Assassin
Automated Supply Chain Triage & Procurement Intelligence

The Problem
Legacy ERP and Warehouse Management Systems (WMS) excel at tracking data but fail at generating actionable intelligence. Standard systems output massive, unfiltered spreadsheet dumps, forcing procurement teams to spend hours manually filtering rows, identifying low stock, and manually cross-referencing suppliers to build efficient purchase orders. This administrative friction leads to delayed orders, split-shipping fees, and missed freight minimums.

The Solution
Excel Assassin is a Python-based web application that bridges the gap between raw data and executive action. It ingests standard inventory exports, automatically isolates at-risk items, groups them logically by vendor, and uses Generative AI to deliver a concise, plain-English procurement briefing.

Target Audience: Supply Chain Managers, Procurement Specialists, and small-to-midsize distributors looking to eliminate spreadsheet waste and optimize purchasing cycles.

Key Features
Automated Data Triage: Upload raw .csv or .xlsx files and instantly filter inventory against custom stock thresholds using the Pandas data engine.

Vendor Consolidation: Automatically groups critical items by Supplier/Vendor, enabling buyers to instantly draft consolidated Purchase Orders to hit prepaid freight minimums.

AI-Driven Briefings: Integrates Google's modern Generative AI SDK (gemini-2.5-flash) to analyze the filtered data and generate a strategic, actionable reorder summary.

Modern UI: Clean, responsive, and easily scannable dashboard built with Tailwind CSS, designed specifically for fast-paced warehouse environments.

Tech Stack
Backend: Python, Flask, Pandas

AI Integration: Google GenAI SDK (google-genai)

Frontend: HTML5, Tailwind CSS (Utility-First UI)

Deployment: Gunicorn, Render

As of 5/22/2026, we are live at "

The Developer
Cambrien Rhodes | Business Systems Analyst & Operations Specialist

This project was built to solve real-world problems. With over 7 years of hands-on experience managing warehouse operations, logistics, and inventory control, I transitioned into software development to build the tools I wish I had on the loading dock. I specialize in identifying systemic operational bottlenecks and deploying targeted Python, Data Analytics, and AI solutions to eliminate them.

Connect with me on LinkedIn: [www.linkedin.com/in/cambrien-rhodes-895358199]
