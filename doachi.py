import photoshop.api as ps
 
def hello_world(): 
    app = ps.Application()
    #doc = app.documents.add() #增加一个文件 
    doc = app.documents[0] #选择第一个打开文件
    
    text_color = ps.SolidColor()
    text_color.rgb.green = 255
    filedir = 6
    new_text_layer = doc.layers[filedir] #第一个图层 
    # new_text_layer = doc.artLayers.add()
    # new_text_layer.kind = ps.LayerKind.TextLayer 
    forindex =0
    with open('achi.txt', 'r', encoding='utf-8') as f:
        for ann in f.readlines():
            forindex+=1
            ann = ann.strip('\n').lower()#.upper()        #去除文本中的换行符
            print(ann)
            new_text_layer.textItem.contents = ann
            
            # new_text_layer.textItem.position = [160, 167]
            # new_text_layer.textItem.size = 40
            # new_text_layer.textItem.color = text_color
            options = ps.PNGSaveOptions(interlaced=False, compression=6)
            index = '0'
            if forindex<10 :
                index ="00"+str(forindex)
            else:
                index ="0"+str(forindex)
                
            png = 'd:/称号/'+str(filedir)+'/'+"Title"+index+'.png'
            doc.saveAs(png, options, asCopy=True)
            
            # app.doJavaScript(f'alert("save to jpg: {png}")')
 
if __name__ == '__main__':
    hello_world() 