import shapefile
w=shapefile.Writer('soal10',shapeType=5)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.record("crot","dua")
w.record("nying","tiga")
w.record("ahhh","empat")
w.record("uhhh","lima")
w.poly([[[1,4],[5,4], [5,5],[1,5],[1,4]]])
w.poly([[[1,9],[5,9], [5,7],[1,7],[1,9]]])
w.poly([[[-1,4],[-5,4], [-5,5],[-1,5],[-1,4]]])
w.poly([[[-1,9],[-5,9], [-5,8],[-1,8],[-1,9]]])
w.poly([[[2,-2],[5,-2], [5,-4],[2,-4],[2,-2]]])
w.close()