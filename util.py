import contextily as ctx
import json


def add_basemap(ax, zoom, url='http://tile.stamen.com/terrain/tileZ/tileX/tileY.png'):
    xmin, xmax, ymin, ymax = ax.axis()
    basemap, extent = ctx.bounds2img(xmin, ymin, xmax, ymax, zoom=zoom, url=url)
    ax.imshow(basemap, extent=extent, interpolation='bilinear')
    ax.axis((xmin, xmax, ymin, ymax))


def export_chart_json(df):
    output = {
        "labels": list(df.iloc[0]),
        "datasets": []
    }

    for i, row in df[1:].iterrows():
        values_dict = {}
        values_dict["label"] = "{}".format(i)
        values_dict["data"] = [round(n,1) for n in list(row)]
        values_dict["fill"] = False
        
        output["datasets"].append(values_dict)

    return json.dumps(output)