"""
COO Module View — reusable full-screen panel for all COO modules.
Extends the base ModuleView with COO-specific styling.
"""

from views.module_view import ModuleView


class COOModuleView(ModuleView):
    """Inherits ModuleView entirely — same layout, same table.
    Kept as a separate class so COO-specific behaviour can be
    added later without touching the shared ModuleView."""

    pass
