# Table of Content for `graph_objs_meta.py`

## Section -- Required module(s)

## Section  -- Shortcuts definitions and inventories:

### Meta generation shortcuts

Label of top of subsection: `@meta-shortcut@`

+ Function that formats the keys' values into a dictionary (`@output@`)
+ (long string shortcut coming soon)

### Inventory of value types 

Label of top of subsection: `@val_types@`

+ Formatting function for 'number' type (`@val_types-number@`)
+ Value type dictionary (`@val_types-dict@`)

### Shortcut to described conditionally required keys
 
Label of top subsection: `@required_cond@`

+ Formatting function for condition involving keys (`@required_cond-keys@`)
+ Formatting function for condition involving plot type (`@required_cond-plottype@`)
+ Conditionally required dictionary (`@required_cond-dict@`)

### Inventory of meta generators for repeated keys
  
Label of top of subsection: `@shortcuts@` 

Label of specific key shortcut: `@<key>@` e.g. `@x@` for the `'x'` key

#### (fill in shortcut 'categories' e.g. @shortcuts-coordinates@)

## Section -- Graph Objects Meta:

### 'Trace' graph objects
  
Label of top of subsection: `@graph-objs-meta-trace@`

+ Scatter (`@Scatter@`)
+ Bar (`@Bar@`)
+ Histogram (`@Histogram@`)
+ Bar (`@Box@`)
+ Heatmap (`@Heatmap@`)
+ Contour (`@Contour@`)
+ Histogram2d (`@Histogram2d@`)
+ Histogram2dContour (`@Histogram2dContour@`)
+ Area (`@Area@`)

### 'Auxiliary trace' graph objects

Label of top of section: `@graph-objs-meta-trace-aux@`

#### Error (`@Error@`)

+ ErrorY (`@ErrorY@`)
+ ErrorX (`@ErrorX@`)

#### Bins (`@Bins`)

+ XBins (`@XBins@`)
+ YBins (`@YBins@`)

#### 

+ Contours (`@Contours@`)
+ Stream (`@Stream@`)

### 'Style' graph objects 

Label of top of section: `@graph-objs-meta-style @`

+ Marker (`@Marker@`)
+ Line (`@Line@`)
+ Font (`@Font@`)

### 'Axis' graph objects  

Label of top of section: `@graph-objs-meta-layout-axis@`

#### TICKS (`@TICKS@`)

#### AXIS (`@Axis@`)

####

+ XAxis (`@XAxis@`)
+ YAxis (`@YAxis@`)
+ RadialAxis  (`@RadialAxis`)
+ AngularAxis (`@AngularAxis`)

### Other 'auxiliary layout' graph objects 

Label of top of section: `@graph-objs-meta-layout-aux@`

+ Legend (`@Legend`)
+ ColorBar (`@ColorBar`)
+ Margin (`@Margin`)
+ Annotation (`@Annotation`)

* Layout (`@Layout`)

* Figure (`@Figure`)

### Other graph objects 

Label of top of section: `@graph-objs-meta-others`

+ Data (`@PlotlyData`)
+ Annotations (`@Annotations`)
+ Trace (`@Trace`)
+ PlotlyList (`@PlotlyList`)
+ PlotlyDict (`@PlotlyDict`)
+ PlotlyTrace (`@PlotlyTrace`)

## Section -- Write to JSON
