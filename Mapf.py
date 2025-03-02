import random
import processing
import time
from PyQt5.QtCore import QTimer
from qgis.core import QgsProject

def showBusD (current_time,D_pgr):
    if current_time == '7:50':
        if(D_pgr>40):
            proj = QgsProject.instance()
            layer1 = QgsProject.instance().mapLayersByName('750D')[0]
            layer2 = proj.mapLayersByName('740C')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('75``0D')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(40000)
    elif current_time == '10:10':
        if(D_pgr>40):
            proj = QgsProject.instance()
            layer1 = QgsProject.instance().mapLayersByName('1010D')[0]
            layer2 = proj.mapLayersByName('740C')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('1010D')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    elif current_time == '12:30':
        if(D_pgr>40):
            proj = QgsProject.instance()
            layer1 = QgsProject.instance().mapLayersByName('1230D')[0]
            layer2 = proj.mapLayersByName('740C')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('1230D')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    elif current_time == '2:50':
        if(D_pgr>40):
            proj = QgsProject.instance()
            layer1 = QgsProject.instance().mapLayersByName('250D')[0]
            layer2 = proj.mapLayersByName('740C')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('250D')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    elif current_time == '5:10':
        if(D_pgr>40):
            layer1 = QgsProject.instance().mapLayersByName('510D')[0]
            layer2 = proj.mapLayersByName('740C')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('510D')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    else:
        print(f'\nNo schedule for Bus D found')
def mlayer(layer1,layer2):
    print(f'\nThreshold crossed! Merging routes...')
    
    # Run the merge algorithm
    merged_layer = processing.run("qgis:mergevectorlayers", {'LAYERS': [layer1, layer2], 'CRS': layer1.crs(), 'OUTPUT': 'memory:'})['OUTPUT']

    # Copy the symbology from the first layer to the merged layer
    layer1_renderer = layer1.renderer().clone()
    merged_layer.setRenderer(layer1_renderer)

    # Add the merged layer to the map
    QgsProject.instance().addMapLayer(merged_layer)

    # Refresh the map canvas
    iface.mapCanvas().refresh()
    timer = QTimer()
    timer.timeout.connect(lambda: hideBus(merged_layer, timer))
    timer.start(20000)
def hideBus(layer,timer):
    proj = QgsProject.instance()
    proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(False)
    timer.stop()

def showBusA2(current_time,ex_t,a_t):
    if current_time == '7:50':
        alert = "\nAdmin alert initiated, extending route time for A2" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('750A2')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(40000+ex_t)
    elif current_time == '11:20':
        alert = "\nAdmin alert initiated, extending route time for A2" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('1120A2')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    elif current_time == '2:50':
        alert = "\nAdmin alert initiated, extending route time for A2" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('250A2')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    elif current_time == '4:10':
        alert = "\nAdmin alert initiated, extending route time for A2" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('410A2')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    elif current_time == '6:30':
        alert = "\nAdmin alert initiated, extending route time for A2" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('630A2')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    else:
        print(f'\nNo schedule for Bus A2 found')

def showBusA1(current_time,ex_t,a_t):
    if current_time == '7:40':
        alert = "\nAdmin alert initiated, extending route time for A1" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('740')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    elif current_time == '11:20':
        alert = "\nAdmin alert initiated, extending route time for A1" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('1120')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    elif current_time == '2:50':
        alert = "\nAdmin alert initiated, extending route time for A1" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('250')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    elif current_time == '4:10':
        alert = "\nAdmin alert initiated, extending route time for A1" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('410')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    elif current_time == '6:30':
        alert = "\nAdmin alert initiated, extending route time for A1" if a_t==1 else " "
        print(alert)
        proj = QgsProject.instance()
        layers = proj.mapLayersByName('630')
        layer = layers[0]
        proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
        timer = QTimer()
        timer.timeout.connect(lambda: hideBus(layer, timer))
        timer.start(30000+ex_t)
    else:
        print(f'\nNo schedule for Bus A1 found')

def showBusC (current_time,C_pgr):
    if current_time == '7:40':
        if(C_pgr>40):
            proj = QgsProject.instance()
            layer1 = QgsProject.instance().mapLayersByName('740C')[0]
            layer2 = proj.mapLayersByName('750D')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('740C')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    elif current_time == '9:00':
        if(C_pgr>40):
            proj = QgsProject.instance()
            layer1 = QgsProject.instance().mapLayersByName('900C')[0]
            layer2 = proj.mapLayersByName('750D')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('900C')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    elif current_time == '11:20':
        if(C_pgr>40):
            proj = QgsProject.instance()
            layer1 = QgsProject.instance().mapLayersByName('1120C')[0]
            layer2 = proj.mapLayersByName('750D')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('1120C')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    elif current_time == '1:40':
        if(C_pgr>40):
            proj = QgsProject.instance()
            layer1 = QgsProject.instance().mapLayersByName('140C')[0]
            layer2 = proj.mapLayersByName('750D')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('140C')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    elif current_time == '4:00':
        if(C_pgr>40):
            layer1 = QgsProject.instance().mapLayersByName('400C')[0]
            layer2 = proj.mapLayersByName('750D')[0]
            mlayer(layer1,layer2)
        else:
            proj = QgsProject.instance()
            layers = proj.mapLayersByName('400C')
            layer = layers[0]
            proj.layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(True)
            timer = QTimer()
            timer.timeout.connect(lambda: hideBus(layer, timer))
            timer.start(30000)
    else:
        print(f'\nNo schedule for Bus C found')

# - - - Main - - -

bus_schedule = ['7:40', '7:50', '9:00','10:10','11:20','12:30','1:40',
                 '2:50','4:00','4:10','5:10', '6:30']  #Bus Schedules
                 
pgr = [20,25,30,35,40,45,50]   #passenger counts
admin_trigger = [0,1]          #admin trigger

# Randomly generated values
current_time = random.choice(bus_schedule)
C_pgr = random.choice(pgr)
D_pgr = random.choice(pgr)
a_t = random.choice(admin_trigger)
print(f'Random values generated are:\n')
print(f'\nPassengers in BUS C : {C_pgr}')
print(f'\nPassengers in BUS D : {D_pgr}')
print(f'\nAdmin trigger : {a_t}')
print(f"\n\nDisplaying routes for all buses at {current_time}\n")

if(a_t == 1):
    ex_t = 20000
    showBusA1(current_time,ex_t,a_t)
    showBusA2(current_time,ex_t,a_t)
else:
    ex_t = 0
    showBusA1(current_time,ex_t,a_t)
    showBusA2(current_time,ex_t,a_t)

showBusC(current_time,C_pgr)
showBusD(current_time,D_pgr)