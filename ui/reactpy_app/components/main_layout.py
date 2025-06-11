from reactpy import component, html

@component  
def MainLayout():
    """Main application layout component."""
    return html.div(
        {"class": "min-h-screen bg-gray-100"},
        html.header(
            {"class": "bg-white shadow"},
            html.div(
                {"class": "max-w-7xl mx-auto py-6 px-4"},
                html.h1(
                    {"class": "text-3xl font-bold text-gray-900"},
                    "LLM Trainer MVP"
                )
            )
        ),
        html.main(
            {"class": "max-w-7xl mx-auto py-6 px-4"},
            html.div(
                {"class": "bg-white rounded-lg shadow p-6"},
                html.h2(
                    {"class": "text-xl font-semibold mb-4"},
                    "Training Pipeline"
                ),
                html.p(
                    {"class": "text-gray-600"},
                    "Welcome to the LLM Trainer MVP. This is a local-first fine-tuning framework."
                )
            )
        )
    )
