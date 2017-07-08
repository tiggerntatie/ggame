def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

if module_exists('browser') and module_exists('javascript'):

    from browser import window, document
    from javascript import JSObject, JSConstructor
    major = window.__BRYTHON__.implementation[0]
    minor = window.__BRYTHON__.implementation[1]
    if major == 3 and minor >= 3 or major > 3:
        GFX = window.PIXI
        GFX_Rectangle = GFX.Rectangle.new
        GFX_Texture = GFX.Texture.new
        GFX_Texture_fromImage = GFX.Texture.fromImage.new
        GFX_Sprite = GFX.Sprite.new
        GFX_Graphics = GFX.Graphics.new()
        GFX_Text = GFX.Text.new
        GFX_NewStage = GFX.Container
        SND = window.buzz
        SND_Sound = SND.sound.new
    else:
        GFX = JSObject(window.PIXI)
        GFX_Rectangle = JSConstructor(GFX.Rectangle)
        GFX_Texture = JSConstructor(GFX.Texture)
        GFX_Texture_fromImage = JSConstructor(GFX.Texture.fromImage)
        GFX_Sprite = JSConstructor(GFX.Sprite)
        GFX_Graphics = JSConstructor(GFX.Graphics)()
        GFX_Text = JSConstructor(GFX.Text)
        GFX_NewStage = JSConstructor(GFX.Container)
        SND = JSObject(window.buzz)
        SND_Sound = JSConstructor(SND.sound)
    GFX_DetectRenderer = GFX.autoDetectRenderer 
  
    class GFX_Window(object):
        
        def __init__(self, width, height, onclose):
            self._w = window.open("", "")
            GFX.utils._saidHello = True; # ugly hack to block pixi banner
            self._stage = GFX.NewStage()
            self.width = width if width != 0 else int(window.innerWidth * 0.9)
            self.height = height if height != 0 else int(window.innerHeight * 0.9)
            self._renderer = GFX.autoDetectRenderer(self.width, self.height, {'transparent':True, 'antialias':True})
            self._w.document.body.appendChild(self._renderer.view)
            self._w.onunload = onclose
      
        def bind(self, evtspec, callback):
            self._w.document.body.bind(evtspec, callback)
          
        def add(self, obj):
            self._stage.addChild(obj)
          
        def remove(self, obj):
            self._stage.removeChild(obj)
          
        def animate(self, stepcallback):
            self._renderer.render(self._stage)
            self._w.requestAnimationFrame(stepcallback)
          
        def destroy(self):
            SND.all().stop()
            self._stage.destroy()
  

elif module_exists('pygame'):

    try:
        from ggame.pygamedeps import *
    except:
        from pygamedeps import *

else:
    try:
        from ggame.headlessdeps import *
    except:
        from headlessdeps import *
  
    
