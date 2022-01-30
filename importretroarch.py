import os

shaders = []
for root, dirs, files in os.walk('../glsl-shaders'):
  for fn in files:
    if fn.endswith('.glslp'):
      with open(root + '/' + fn) as f:
        for l in f:
          ws = l.split()
          if not ws:
            continue
          if ws[0] == 'shader1':
            break
          if ws[0] == 'shader0':
            shader = ws[2]
        else:
          lines = [
              '#define VertexCoord vec4(position,1)\n',
              '#define TexCoord vec2(uv.x, 1.-uv.y)\n',
          ]
          with open(root + '/' + shader.strip('"'), encoding='iso-8859-1') as f:
            for l in f:
              l = l.replace('__VERSION__ >= 130', '__VERSION__ >= 1300')
              nono = [
                  'vec2 TexCoord',
                  'vec4 TexCoord',
                  'vec4 VertexCoord',
                  '#pragma',
                  '#version',
              ]
              if all(n not in l for n in nono):
                lines.append(l)
          with open('shaders/' + fn[:-1], 'w') as f:
            f.writelines(lines)
          shaders.append(fn[:-6])
print('\n'.join(sorted(shaders)))
