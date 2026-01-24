from uuid import uuid4
from app.settings import get_session
from app.models import (
    ModuleState, ModuleModel,
    StepState, StepModel
)


def seed_module():
    m1 = ModuleModel(
        id=uuid4(),
        state=ModuleState.DRAFT,
        title='NetworkX Basics',
        slug='networkx-basics',
        overview='Изучим популярную библиотеку для работы с графами.',
        summary="Настроим окружени и изучим топовую бибилотеку для работы с графами."
    )
    s1 = StepModel(
        id=uuid4(),
        module_id=m1.id,
        state=StepState.DRAFT,
        title='Введение в графы',
        slug='introduction-to-graphs',
        overview='Введение в графы',
        summary='Введение в графы'

    )
    s2 = StepModel(
        id=uuid4(),
        module_id=m1.id,
        state=StepState.DRAFT,
        title='Обход графов: DFS и BFS',
        slug='graph-traversal-dfs-bfs',
        overview='Изучение алгоритмов обхода графов: поиск в глубину и в ширину.',
        summary='Реализация и применение DFS и BFS.'
    )
    s3 = StepModel(
        id=uuid4(),
        module_id=m1.id,
        state=StepState.DRAFT,
        title='Кратчайшие пути: Дейкстра и Флойд-Уоршелл',
        slug='shortest-paths-dijkstra-floyd',
        overview='Алгоритмы поиска кратчайших путей в взвешенных графах.',
        summary='Работа с алгоритмами Дейкстры и Флойда-Уоршелла.'
    )
    with get_session() as session:
        session.add(m1)
        session.add_all([s1, s2, s3])
