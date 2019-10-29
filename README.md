# wind-turbine_design_optimization

The 3rd Evolutionary Computation Competition  The problem is a wind turbine design optimization problem.  
http://www.jpnsec.org/files/competition2019/EC-Symposium-2019-Competition.html

## ディレクトリ構造
```
wind-turbine_design_optimization/
  ┣━━ EC2019/    ...    構築された評価用環境ディレクトリ
  ┣━━ evaluation/
  ┃     ┣━━ windturbine_SOP.py    ...    評価モジュール
  ┃     ┣━━ pop_vars_eval.txt
  ┃     ┣━━ pop_objs_eval.txt
  ┃     ┗━━ pop_cons_eval.txt
  ┣━━ src/
  ┃     ┣━━ DE.py    ...    メインスクリプト
  ┃     ┣━━ file_handler.py    ...    write/read用関数
  ┃     ┣━━ setting.py    ...    ハイパーパラメータなど
  ┃     ┗━━ evaluation.bat    ...    WSL上でPython2.7環境を呼び出し評価モジュールを動かすスクリプト
  ┣━━ logs/    ...    ログ(csv)の格納場所
  ┣━━ README.md    ...    このファイル
  ┗━━ EC2019_build_env.md    ...    環境構築手引書
```