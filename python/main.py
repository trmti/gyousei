from linebot import (
    LineBotApi,
)

from linebot.models import (
    RichMenu,
    RichMenuArea,
    RichMenuSize,
    RichMenuBounds,
    MessageAction,
)
from linebot.models.actions import RichMenuSwitchAction
from linebot.models.rich_menu import RichMenuAlias

import rich_menu_object

line_bot_api = LineBotApi('zxPozaYSp7Rv03isLXbtd8H4z5Nfq79SCRVVuCfrhhhqB1GTzfEtERa8pihhqLgrRMU1thPnzLMeuYJ1NrrzUBSO9X3uGPuvSRvsiRPbIfw6c462fy08iDk2HyNedpRw1CaBqgY2Rrz3+Oe3TCFEHgdB04t89/1O/w1cDnyilFU=') # 上書きする

def reset():
    # 全 alias を選択する
    rich_menu_list = line_bot_api.get_rich_menu_list()
    for rich_menu in rich_menu_list:
        # alias を削除する
        line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)

    # 全リッチメニューを選択する
    for rich_menu_alias in line_bot_api.get_rich_menu_alias_list().aliases:
        # リッチメニューを削除する
        line_bot_api.delete_rich_menu_alias(rich_menu_alias.rich_menu_alias_id)

# アクションの登録
def create_action(action):
    return MessageAction(type=action['type'], label=action['label'], text=action["text"])
    
# rich_menu_object でリッチメニューの構成を指定する
# リッチメニューオブジェクト: https://developers.line.biz/ja/reference/messaging-api/#rich-menu-object
def create_rich_menus(rich_menu_object):
    areas = [
        RichMenuArea(
            bounds=RichMenuBounds(x=info['bounds']['x'], y=info['bounds']['y'], width=info['bounds']['width'], height=info['bounds']['height']),
            action=create_action(info['action'])
        ) for info in rich_menu_object['areas']
    ]

    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=rich_menu_object['size']['width'], height=rich_menu_object['size']['height']),
        selected=rich_menu_object['selected'],
        name=rich_menu_object['name'],
        chat_bar_text=rich_menu_object['name'],
        areas=areas
    )
    return line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)

# リッチメニューに画像をアップロードする
def set_rich_menu_image(rich_menu_id, rich_menu_image_path):
    with open(rich_menu_image_path, 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)

# デフォルトのリッチメニューを設定する
def set_default_rich_menu(rich_menu_id):
    line_bot_api.set_default_rich_menu(rich_menu_id)

# リッチメニューの alias の登録
def set_rich_menus_alias(rich_menu_id, rich_menus_alias_id):
    alias = RichMenuAlias(
        rich_menu_alias_id=rich_menus_alias_id,
        rich_menu_id=rich_menu_id
    )
    line_bot_api.create_rich_menu_alias(alias)

def main():
    # 2. リッチメニューA（richmenu-a）を作成する
    rich_menu_a_id = create_rich_menus(rich_menu_object.rich_menu_object_a())
    # 3. リッチメニューAに画像をアップロードする
    set_rich_menu_image(rich_menu_a_id, '../public/shako.png')
    # 6. リッチメニューAをデフォルトのリッチメニューにする
    set_default_rich_menu(rich_menu_a_id)
    # 7. リッチメニューエイリアスAを作成する
    set_rich_menus_alias(rich_menu_a_id, 'richmenu-alias-a')
    print('success')

reset()
main()