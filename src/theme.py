import altair as alt

def lac_theme():
    return {
        "config": {

            "title": {
                "fontSize": 13,                    
                "fontWeight": "normal",
                "anchor": "middle",                     
                "color": "#1F2937",
                "font": "Inter, Helvetica, Arial, sans-serif",
                "subtitleFontSize": 12,
                "subtitleColor": "#4B5563",
                "subtitleFont": "Inter, Helvetica, Arial, sans-serif",
                "subtitlePadding": 2,                   # tighter spacing
                "subtitleLineHeight": 15
            },

            "text": {
                "fontSize": 11,
                "fontWeight": "normal",
                "font": "Inter, Helvetica, Arial, sans-serif",
                "color": "#1F2937",
                "align": "center",
                "baseline": "middle"
            },

            "axis": {
                "labelFontSize": 11,
                "titleFontSize": 10,
                "grid": True,
                "gridColor": "#ECEFF4",
                "domainColor": "#B0BEC5",
                "tickColor": "#B0BEC5",
                "labelColor": "#374151",
                "titleColor": "#374151",
                "labelAlign": "center",
                "titleAlign": "center",
                "labelPadding": 4
            },


            "axisX": {
                "labelAngle": 0,                       
                "labelAlign": "center",
                "labelBaseline": "top",
                "labelPadding": 6,
                "tickSize": 3
            },


            "legend": {
                "titleFontSize": 11,
                "labelFontSize": 10,
                "cornerRadius": 6,
                "orient": "top",                     
                "direction": "horizontal",              
                "titleAnchor": "middle",               
                "labelAlign": "center",
                "titleAlign": "center",
                "padding": 4,
                "symbolSize": 90,
                "symbolType": "square",
                "symbolStrokeWidth": 0.3,
                "titleColor": "#1F2937",
                "labelColor": "#374151",
                "columns": 3,                           
                "columnPadding": 10,
                "symbolLimit": 200
            },


            "view": {
                "stroke": None,
                "fill": "transparent"
            },

            "geoshape": {
                "fill": "#f9f9f9",
                "stroke": "#cccccc",
                "strokeWidth": 0.4
            },

            "range": {
                "category": {"scheme": "tableau10"},
                "heatmap": {"scheme": "blues"},
                "diverging": {"scheme": "redblue"},
                "ramp": {"scheme": "blues"}
            },

            "mark": {
                "opacity": 0.9
            }
        }
    }

alt.themes.register("lac_theme", lac_theme)
alt.themes.enable("lac_theme")
