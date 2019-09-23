"""
Just Add the func for your own template Lol

you can design at
https://developers.line.biz/console/fx/

thx to me arsybai hehe :3
"""
class flexTemplate:

  def __init__(self):
    return None

  def contoh(self):
    this = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://net.avakinworld.com/images/bg_1.jpg",
            "size": "5xl",
            "aspectMode": "cover",
            "aspectRatio": "150:196",
            "gravity": "center",
            "flex": 1,
            "action": {
              "type": "uri",
              "uri": "https://net.avakinworld.com/"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://net.avakinworld.com/images/bg_2.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                  "action": {
                    "type": "uri",
                    "uri": "https://net.avakinworld.com/"
                  }
              },
              {
                "type": "image",
                "url": "https://net.avakinworld.com/images/2.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "150:98",
                "gravity": "center",
                  "action": {
                    "type": "uri",
                    "uri": "https://net.avakinworld.com/"
                  }
              }
            ],
            "flex": 1
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://net.avakinworld.com/images/about.jpg",
                "aspectMode": "cover",
                "size": "full",
                  "action": {
                    "type": "uri",
                    "uri": "line://ti/p/%40cbl8900e"
                  }
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "#AvakinNews",
                    "weight": "bold",
                    "color": "#000000"
                  },
                  {
                    "type": "span",
                    "text": "     "
                  },
                  {
                    "type": "span",
                    "text": "Sumber informasi tentang Avakin Life, Player, beserta Perkembangannya."
                  }
                ],
                "size": "sm",
                "wrap": true,
                  "action": {
                    "type": "uri",
                    "uri": "line://ti/p/%40cbl8900e"
                  }
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Kambing Jones®",
                    "size": "sm",
                    "color": "#bcbcbc"
                  }
                ],
                "spacing": "sm",
                "margin": "md"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px"
  }
}
    return this
