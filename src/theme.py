import altair as alt

def lac_theme():
    return {
        "config": {
            # ----- TITLE -----
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
            # ----- TEXT LABELS -----
            "text": {
                "fontSize": 11,
                "fontWeight": "normal",
                "font": "Inter, Helvetica, Arial, sans-serif",
                "color": "#1F2937",
                "align": "center",
                "baseline": "middle"
            },
            # ----- NUMBER FORMATTING -----
            # This affects numeric labels, axes, legends, tooltips, etc.
            "numberFormat": ".1f",  # 👈 one decimal everywhere
            # ----- VIEW FRAME -----
            "view": {"stroke": None},
            # ----- AXES -----
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
            # ----- LEGEND -----
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
            # ----- COLOR SCHEME -----
            "range": {
                "category": {"scheme": "tableau10"}
            },
            # ----- BACKGROUND -----
            "background": "white",
        }
    }

alt.themes.register("lac_theme", lac_theme)
alt.themes.enable("lac_theme")
