import module.frontview as frontview
import module.rearview as rearview
import module.emergencty as emerency

def __main__():
        fv = frontview.FrontView()
        rv = rearview.RearView()
        emer = emergency.Emergency()
        while True:
                rv.showview()
		
