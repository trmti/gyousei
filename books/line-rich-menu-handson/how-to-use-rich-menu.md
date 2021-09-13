---
title: "リッチメニューでできること"
---

## 3種類のリッチメニュー
### 優先順位を決めることができる
3種類のリッチメニューがあり、それぞれ次の順に表示される

1. 「Messaging APIで設定するユーザー単位」
2. 「Messaging APIで設定するデフォルト」
3. 「LINE Official Account Managerで設定するデフォルト」

| タイプ | 反映されるタイミング |
| :--- | :--- |
| Messaging APIで設定するユーザー単位のリッチメニュー | 即時。ただし、ユーザーとのリンクを解除せずにリッチメニューを削除した場合は、トーク画面に再入室したときに削除が反映されます。 |
| Messaging APIで設定するデフォルトのリッチメニュー | トーク画面に再入室したとき。変更が反映されるまで、1分程度掛かる場合があります。 |
| LINE Official Account Managerで設定するデフォルトのリッチメニュー | トーク画面に再入室したとき。 |

参考：[リッチメニューの表示について](https://developers.line.biz/ja/docs/messaging-api/using-rich-menus/#rich-menu-display)

## 同期的にリッチメニューを入れ替えることができる
「Messaging APIで設定するユーザー単位」を利用することで、リッチメニュー同士での切り替えができるようになったため、リッチメニューのページ遷移ができるようになった。

## リッチメニューの追加
API側からユーザーごとにリッチメニューを登録ができる。つまり「画像にユーザー名を入れたり特有の動線を入れることが可能になる」「ボタンを押したアクションをカスタム」などなど幅が広がりました。