import pykka, time, sys, logging
from mopidy.core import CoreListener
from lcd_class import Lcd

logger = logging.getLogger('moplcd')

class moplcdFrontend(pykka.ThreadingActor, CoreListener):
        def __init__(self, config, core):
                super(moplcdFrontend, self).__init__()
                logger.info("moplcd initialising")
                self.core = core
                self.config = config
                stderr = sys.stderr.write;
                self.lcd = Lcd()

                # Try to trap any exit errors and cleanup GPIO
                def exit_fn():
                        if not traceback.format_exc().startswith('None'):
                                s=traceback.format_exc()

                # Register
                #atexit.register(exit_fn)

                def interrupt():
                        return False

                boardrevision = 2

                self.lcd.init(boardrevision)
                self.lcd.setWidth(20)
                self.lcd.setRawMode(True) # Neu eingefügt
                self.lcd.line1("    Pi Music Box")
                self.lcd.line2(time.strftime(" %d.%m.%Y - %H:%M"))
                self.lcd.line3("Initialisiere...")
                self.lcd.line4("")
                
        def stream_title_changed(self, tl_track):
                #logger.info("track playback startet")
                #self.lines.track(True, "track name")
                #self.lines.time()
                self.lcd.line3(tl_track)

        def on_start(self): 
                #self.lines.startstop(True)
        
        def on_stop(self):
                #self.lines.startstop(False)
                
        def track_playback_paused(self, tl_track, time_position):
                
                #self.lines.track(False, "Pause")
                #self.lines.time()
                self.lcd.line4('Paused')
        
        def track_playback_resumed(self, tl_track, time_position):
                
                #self.lines.track(True, "Play")
                #self.lines.time()
                self.lcd.line4('Resumed')
