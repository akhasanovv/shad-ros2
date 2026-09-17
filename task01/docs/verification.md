# L01 · verification

Student ID: ...  
Commit SHA: ...

## Обязательные проверки

- `course test --case found`: 
```json
{"id": "found", "max_points": 55, "points": 55, "status": "pass", "metrics": {"execution_seconds": 25.7, "position_error_m": 0.013986, "explicit_stop": true}, "wall_seconds": 26.6}
```
- `course test --case absent`: 
```json
{"id": "absent", "max_points": 45, "points": 45, "status": "pass", "metrics": {"execution_seconds": 45.98, "explicit_stop": true}, "wall_seconds": 46.85}
```

## Известная граница решения

Одно короткое ограничение или ещё не выполненный bonus: да вроде нет ограничений, если верить в то, что black box функции корректно отрабатывают. 

## Использование LLM
Какие части помогал писать LLM и какими core tests они проверены: просто спрашивал у codex, что вообще происходит, тк сначала начал сам писать логику обхода грида змейкой...
Не нужны приватные промпты или рассуждения модели.
