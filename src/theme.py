import altair as alt

def lac_theme():
    return {
        "config": {
           
            "title": {
                "fontSize": 18,
                "fontWeight": "normal",
                "anchor": "middle",
                "color": "#1F2937",
                "align":"center",
                "font": "Inter, Helvetica, Arial, sans-serif",
                "subtitleFontSize": 13,
                "subtitleColor": "#4B5563"
            },
            
            "text": {
                "fontSize": 11,
                "fontWeight": "normal",
                "font": "Inter, Helvetica, Arial, sans-serif",
                "color": "#1F2937",
                "align": "center",
                "baseline": "middle"
            },
        
            
            "numberFormat": ".1f",  
            
            "view": {"stroke": None},
            
            "axis": {
                "labelFontSize": 11,
                "titleFontSize": 12,
                "grid": True,
                "gridColor": "#ECEFF4",
                "domainColor": "#B0BEC5",
                "tickColor": "#B0BEC5",
                "labelColor": "#374151",
                "titleColor": "#374151",
                "labelAlign": "right",  
                "titleAlign": "right"
            },
           
            "legend": {
                "titleFontSize": 12,
                "labelFontSize": 11,
                "cornerRadius": 6,
                "orient": "right",       
                "titleAlign": "left",
                "labelAlign": "left",
                "padding": 10,
                "direction": "vertical"
            },
            
            "range": {
                "category": {"scheme": "tableau10"}
            },
            
            "background": "white",
        }
    }

alt.themes.register("lac_theme", lac_theme)
alt.themes.enable("lac_theme")
