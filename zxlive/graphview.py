#     zxlive - An interactive tool for the ZX calculus
#     Copyright (C) 2023 - Aleks Kissinger
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from pyzx.graph.base import BaseGraph, VT, ET
from .graphscene import GraphScene


class GraphView(QGraphicsView):
    """QtWidget containing a graph

    This widget is view associated with a graph. However, most of the
    interesting stuff happens in `GraphScene`.
    """

    def __init__(self, graph_scene: GraphScene) -> None:
        self.graph_scene = graph_scene
        super().__init__(self.graph_scene)
        self.setMouseTracking(True)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)

    def set_graph(self, g: BaseGraph[VT, ET]) -> None:
        self.graph_scene.set_graph(g)
        self.centerOn(0, 0)
