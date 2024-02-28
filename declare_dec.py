import ipywidgets as widgets
from ipywidgets import interact, interactive, interactive_output
from ipywidgets import Layout, Button, Box, VBox, HBox
from plot_decrate import plot_decrate
# bmix - cp parameters
dm=widgets.BoundedFloatText(value=17.749, min=0, max=20, step=0.001, continuous_update=False, description=r'$\Delta m_{s}$ [ps$^{-1}$]',layout=widgets.Layout(width='200px'))
dg=widgets.BoundedFloatText(value=0.083, min=0, max=1, step=0.001, continuous_update=False, description=r'$\Delta \Gamma_{s}$ [ps$^{-1}$]',layout=widgets.Layout(width='200px'))
gs=widgets.BoundedFloatText(value=0.6608, min=0, max=1, step=0.001, continuous_update=False, description=r'$\Gamma_{s}$ [ps$^{-1}$]',layout=widgets.Layout(width='200px'))
r=widgets.BoundedFloatText(value=0, min=0, max=1, step=0.1, continuous_update=False, description=r'$r$',layout=widgets.Layout(width='200px'))
delta=widgets.BoundedFloatText(value=0, min=0, max=360, step=1, continuous_update=False, description=r'$\delta$ [$\circ$]',layout=widgets.Layout(width='200px'))
gamma=widgets.BoundedFloatText(value=0, min=0, max=360, step=1, continuous_update=False, description=r'$\gamma$ [$\circ$]',layout=widgets.Layout(width='200px'))
beta=widgets.BoundedFloatText(value=0, min=-1000, max=1000, step=1, continuous_update=False, description=r'$\beta_{s}$ [mrad]',layout=widgets.Layout(width='200px'))
k=widgets.BoundedFloatText(value=1, min=0, max=1, step=0.01, continuous_update=False, description=r'$k$',layout=widgets.Layout(width='200px'))
# plotting
xmin=widgets.BoundedFloatText(value=0, min=0, max=100, step=1, continuous_update=False, description=r'$t_{min}$ [ps]',layout=widgets.Layout(width='200px'))
xmax=widgets.BoundedFloatText(value=5, min=0, max=100, step=1, continuous_update=False, description=r'$t_{max}$ [ps]',layout=widgets.Layout(width='200px'))
y_osc=widgets.BoundedFloatText(value=1, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{dec}$ [a.u.]',layout=widgets.Layout(width='200px'))
y_mix=widgets.BoundedFloatText(value=1, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{mix}$ [a.u.]',layout=widgets.Layout(width='200px'))
name=widgets.Text(value='plots/decrate.eps',continuous_update=False,layout=widgets.Layout(width='200px'))#description='Save as:')
save=widgets.ToggleButton(value=False,description='Save',layout=widgets.Layout(width='200px'))
# select
bach=widgets.Text(value=r'\pi',continuous_update=False,description='h:',layout=widgets.Layout(width='200px'))
b_f = widgets.Checkbox(value=True,description=r'$B$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
bbar_f = widgets.Checkbox(value=True,description=r'$\overline{B}$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
bbar_fbar = widgets.Checkbox(value=True,description=r'$\overline{B}$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
b_fbar = widgets.Checkbox(value=True,description=r'$B$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
fold_amix = widgets.Checkbox(value=True,description=r'fold $A_{mix}$',disabled=False,layout=widgets.Layout(width='200px'))
## Decay Rate
wbox_dec = HBox([VBox([gs,dg,dm,fold_amix,bach]),VBox([r,delta,gamma,beta,k]),VBox([xmin,xmax,y_osc,y_mix]),
                 VBox([b_f,bbar_f,bbar_fbar,b_fbar]),VBox([name,save])])
decrate_pars = interactive_output(plot_decrate,{'dm':dm,'dg':dg,'gs':gs,
                                                'r':r,'delta':delta,'gamma':gamma,'beta':beta,'k':k,
                                                'xmin':xmin,'xmax':xmax,'y_osc':y_osc,'y_mix':y_mix,
                                                'name':name,'save':save,
                                                'bach':bach,
                                                'b_f':b_f,
                                                'bbar_f':bbar_f,
                                                'bbar_fbar':bbar_fbar,
                                                'b_fbar':b_fbar,
                                                'fold_amix':fold_amix})
