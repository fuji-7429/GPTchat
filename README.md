"# GPTchat" 

streamlitとChatGPT APIを組み合わせたアプリケーション


# 実装内容
- チャットAIの作成
  - 自作のチャットAIとstreamlit公式のチャットアプリプログラムを実装
- 自作のものとページ切り替えで使用できるように実装
  - main.pyを実行すればページ切り替えで両方使用可能
  - 各pythonファイルを実行すれば、個別に使用可能


# 使用方法
1. チャットAIアプリ単体を使用する場合
   1. `streamlit run app.py`または`streamlit run app2.py`を実行
   2. それぞれ指定したPythonファイルのアプリが起動する
2. チャットアプリ2つともを、ページで遷移できるようにする場合
   1. `streamlit run main.py`を実行
   2. サイドバーで、どちらのアプリを使用するか選択できる
3. frontend,backendで分けた場合
   1. 作成中








現在開発中


今後やりたいこと
- チャットの顔を変える[参考](https://zenn.dev/nishijima13/articles/7ed472f51240b5)
- backendを作る[参考](https://qiita.com/CodingDane/items/5fb0a93833e9152ba070)
- RAGを組み合わせる[参考](https://js2iiu.com/2025/12/19/streamlit-rag-01/#google_vignette)
- 複数のタブを実装し、タブごとで異なる機能を実装
  - タブごとにpythonファイルを分ける[参考](https://js2iiu.com/2026/01/04/streamlit-st-tabs/)
  - 重くならないように、st.cache_data,st.cache_resourceで避ける[参考1](https://js2iiu.com/2026/01/04/streamlit-st-tabs/),[参考2](https://note.com/kenta_1932/n/n15a11d2e09c2#323164af-dad4-4111-a04a-788eb1791743)

