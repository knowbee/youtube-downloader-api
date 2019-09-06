# yt-downloader

Youtube Video Downloader API

## Request & Response Examples

YOUTUBE_VIDEO_URL = "https://www.youtube.com/watch?v=-0NIvxDNNk8"

### API Resources

- [GET /video](#get-video)
- [GET /audio](#get-audio)

### GET /video

Example: https://yt-get.herokuapp.com/video?url="YOUTUBE_VIDEO_URL"

Response body:

    [
      {
        "link": "https://r3---sn-5hne6nsr.googlevideo.com/videoplayback?expire=1567773054&ei=Hv1xXajmLcqsgQe0iqOwDA&ip=37.48.124.13&id=o-AK78BSeowbB5ZJHSmWb-RTLIzkfjbcWTW1kZmWt5P5Y1&itag=22&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-5hne6nsr%2Csn-5hnekn76&ms=au%2Crdu&mv=m&mvi=2&pl=21&initcwndbps=136250&mime=video%2Fmp4&ratebypass=yes&dur=663.765&lmt=1567486359573207&mt=1567751380&fvip=3&fexp=23835867&c=WEB&txp=4535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRQIgeaRQJuQiRAva0XcNMIdqfjFsB2f2sUY7UNP7-0fnzb4CIQDrDUc1haReD7N92trhHs-UFYDbnwTibvBU1c2qrCGTDw%3D%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHylml4wRgIhAOe40nF9CMJp2nYOWNBHzfhTaUS1GLOxIlGBApd1DfnBAiEA0UHqVKk5rg9cBA-bed-J2aGjsjJ5VJ6aoyK6Y-GLgrw%3D&title=BAD+NEWS+ABOUT+THE+DDG+MANSION...",
        "size": "91.5 mb",
        "type": "720p (MP4)"
      },
      {
      "link": "https://r3---sn-5hne6nsr.googlevideo.com/videoplayback?expire=1567773054&ei=Hv1xXajmLcqsgQe0iqOwDA&ip=37.48.124.13&id=o-AK78BSeowbB5ZJHSmWb-RTLIzkfjbcWTW1kZmWt5P5Y1&itag=18&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-5hne6nsr%2Csn-5hnekn76&ms=au%2Crdu&mv=m&mvi=2&pl=21&initcwndbps=136250&mime=video%2Fmp4&gir=yes&clen=40488776&ratebypass=yes&dur=663.765&lmt=1567477075850841&mt=1567751380&fvip=3&fexp=23835867&c=WEB&txp=4531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRgIhAOlByM1mKcGTdu6h2hXeC0RHN36S6vXbUIN-sEJ7IV2bAiEAlgaxdJNunchLvm1Sa_V7QP7biQSSDMZTq9VLG773fEU%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHylml4wRgIhAOe40nF9CMJp2nYOWNBHzfhTaUS1GLOxIlGBApd1DfnBAiEA0UHqVKk5rg9cBA-bed-J2aGjsjJ5VJ6aoyK6Y-GLgrw%3D&title=BAD+NEWS+ABOUT+THE+DDG+MANSION...",
      "size": "12.93 MB",
      "type": "360p (MP4)"
      }
      ]

### GET /audio

Example: https://yt-get.herokuapp.com/audio?url="YOUTUBE_VIDEO_URL"

    [
     {
          "link": "https://r3---sn-5hnekn76.googlevideo.com/videoplayback?expire=1567771275&ei=K_ZxXaWLBpS51wKh_bWIBA&ip=95.211.171.24&id=o-AM16VdYop2Z0-2bwfLKWKjSZ4Dm7OU5pMZ38zUWV_rLy&itag=140&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-5hnekn76%2Csn-5hne6nsr&ms=au%2Crdu&mv=u&mvi=2&pl=25&mime=audio%2Fmp4&gir=yes&clen=10743093&dur=663.765&lmt=1567478478343134&mt=1567749371&fvip=3&keepalive=yes&c=WEB&txp=4531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ALgxI2wwRAIgCfmcNZeQUUpm-74ARcbb5UdePTO9MlGh1uWTSTJyAnACICxgXUrO9-rk3K4fGEGzwP3oPIoEEGYhEVb0J0IuLw_X&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl&lsig=AHylml4wRQIgI_e4gcCK35QrXu2tjLYZS7QQwcV8MvOqZEwRolGuj30CIQDIq_IfvdWETRi2MouGvcjNuvbFTR_FBvdXyVC_n8N5hg%3D%3D&ratebypass=yes&title=BAD+NEWS+ABOUT+THE+DDG+MANSION...",
            "size": "10.25 MB",
            "type": "128 kbps (M4A)"

      },
      {
            "link": "https://r3---sn-5hnekn76.googlevideo.com/videoplayback?expire=1567771275&ei=K_ZxXaWLBpS51wKh_bWIBA&ip=95.211.171.24&id=o-AM16VdYop2Z0-2bwfLKWKjSZ4Dm7OU5pMZ38zUWV_rLy&itag=251&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-5hnekn76%2Csn-5hne6nsr&ms=au%2Crdu&mv=u&mvi=2&pl=25&mime=audio%2Fwebm&gir=yes&clen=10848602&dur=663.721&lmt=1567471711382851&mt=1567749371&fvip=3&keepalive=yes&c=WEB&txp=4511222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ALgxI2wwRQIhALBZCqVogiATLIRRGN1q6pnT7Jza-3kKMzZVUr5woEQAAiAetka4tVYnCq5_v154vSzCyWffzOA5kbvr1pxhkI-ckA%3D%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl&lsig=AHylml4wRQIgI_e4gcCK35QrXu2tjLYZS7QQwcV8MvOqZEwRolGuj30CIQDIq_IfvdWETRi2MouGvcjNuvbFTR_FBvdXyVC_n8N5hg%3D%3D&ratebypass=yes&title=BAD+NEWS+ABOUT+THE+DDG+MANSION...",
              "size": "10.35 MB",
              "type": "160 kbps (WEBM)"
    },
    {
            "link": "https://r3---sn-5hnekn76.googlevideo.com/videoplayback?expire=1567771275&ei=K_ZxXaWLBpS51wKh_bWIBA&ip=95.211.171.24&id=o-AM16VdYop2Z0-2bwfLKWKjSZ4Dm7OU5pMZ38zUWV_rLy&itag=250&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-5hnekn76%2Csn-5hne6nsr&ms=au%2Crdu&mv=u&mvi=2&pl=25&mime=audio%2Fwebm&gir=yes&clen=5398745&dur=663.721&lmt=1567471687450993&mt=1567749371&fvip=3&keepalive=yes&c=WEB&txp=4511222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ALgxI2wwRgIhAPeaTM8XAW5PKQXJuTkmPUCnj4zUr3K0a81e3JfBfvD2AiEAnLUEesDXZdJmMW-aMyl__oIuDaVfV6BElI5hhCv7rLs%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl&lsig=AHylml4wRQIgI_e4gcCK35QrXu2tjLYZS7QQwcV8MvOqZEwRolGuj30CIQDIq_IfvdWETRi2MouGvcjNuvbFTR_FBvdXyVC_n8N5hg%3D%3D&ratebypass=yes&title=BAD+NEWS+ABOUT+THE+DDG+MANSION...",
            "size": "5.15 MB",
            "type": "70 kbps (WEBM)"
    },
    {
            "link": "https://r3---sn-5hnekn76.googlevideo.com/videoplayback?expire=1567771275&ei=K_ZxXaWLBpS51wKh_bWIBA&ip=95.211.171.24&id=o-AM16VdYop2Z0-2bwfLKWKjSZ4Dm7OU5pMZ38zUWV_rLy&itag=249&source=youtube&requiressl=yes&mm=31%2C29&mn=sn-5hnekn76%2Csn-5hne6nsr&ms=au%2Crdu&mv=u&mvi=2&pl=25&mime=audio%2Fwebm&gir=yes&clen=4071904&dur=663.721&lmt=1567471693469173&mt=1567749371&fvip=3&keepalive=yes&c=WEB&txp=4511222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ALgxI2wwRgIhAPKbYTWm4S5mRqjDVvJKCvcazr2R5TctH8XU3WBL2y3LAiEA_W_ZHDC5qi9aPmHPFFaTMZD-oy4OpK7AoHAexzvP9ZA%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl&lsig=AHylml4wRQIgI_e4gcCK35QrXu2tjLYZS7QQwcV8MvOqZEwRolGuj30CIQDIq_IfvdWETRi2MouGvcjNuvbFTR_FBvdXyVC_n8N5hg%3D%3D&ratebypass=yes&title=BAD+NEWS+ABOUT+THE+DDG+MANSION...",
            "size": "3.88 MB",
            "type": "50 kbps (WEBM)"
      }
    ]
