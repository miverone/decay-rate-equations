import ipywidgets as widgets
from ipywidgets import interact, interactive, interactive_output
from ipywidgets import Layout, Button, Box, VBox, HBox
from plot_tagging import plot_tagging
from declare_dec import dm, dg, gs, r, delta, gamma, beta, k
from declare_acc import a_acc, n_acc, b_acc, beta_acc, cutoff_acc
from declare_res import sigma_t

# tagging
omega=widgets.BoundedFloatText(value=0.35, min=0, max=0.5, step=0.01, continuous_update=False, description=r'$\omega_{tag}$',layout=widgets.Layout(width='200px'))
d_omega=widgets.BoundedFloatText(value=0, min=-0.5, max=0.5, step=0.001, continuous_update=False, description=r'$\Delta\omega_{tag}$',layout=widgets.Layout(width='200px'))
eff=widgets.BoundedFloatText(value=0.8, min=0, max=1, step=0.01, continuous_update=False, description=r'$\varepsilon_{tag}$',layout=widgets.Layout(width='200px'))
d_eff=widgets.BoundedFloatText(value=0, min=-0.5, max=0.5, step=0.001, continuous_update=False, description=r'$\Delta\varepsilon_{tag}$',layout=widgets.Layout(width='200px'))
# plotting
xmin=widgets.BoundedFloatText(value=0, min=0, max=100, step=1, continuous_update=False, description=r'$t_{min}$ [ps]',layout=widgets.Layout(width='200px'))
xmax=widgets.BoundedFloatText(value=5, min=0, max=100, step=1, continuous_update=False, description=r'$t_{max}$ [ps]',layout=widgets.Layout(width='200px'))
y_tag=widgets.BoundedFloatText(value=0.4, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{tag}$ [a.u.]',layout=widgets.Layout(width='200px'))
y_untag=widgets.BoundedFloatText(value=0.2, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{untag}$ [a.u.]',layout=widgets.Layout(width='200px'))
y_mix=widgets.BoundedFloatText(value=1, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{mix}$ [a.u.]',layout=widgets.Layout(width='200px'))
name=widgets.Text(value='plots/tagging.eps',continuous_update=False,layout=widgets.Layout(width='200px'))
save=widgets.ToggleButton(value=False,description='Save',layout=widgets.Layout(width='200px'))
# select
b_f = widgets.Checkbox(value=True,description=r'$B$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
bbar_f = widgets.Checkbox(value=True,description=r'$\overline{B}$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
bbar_fbar = widgets.Checkbox(value=True,description=r'$\overline{B}$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
b_fbar = widgets.Checkbox(value=True,description=r'$B$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
fold_amix = widgets.Checkbox(value=True,description=r'fold $A_{mix}$',disabled=False,layout=widgets.Layout(width='200px'))
k_acc= widgets.Checkbox(value=True,description=r'Acceptance',disabled=False,layout=widgets.Layout(width='200px'))
k_res= widgets.Checkbox(value=True,description=r'Resolution',disabled=False,layout=widgets.Layout(width='200px'))

## Flavoure Tagging
wbox_tag = HBox([VBox([omega,d_omega,eff,d_eff]),
                 VBox([xmin,xmax,y_tag,y_untag,y_mix]),
                 VBox([k_acc,k_res,fold_amix]),
                 VBox([b_f,bbar_f,bbar_fbar,b_fbar]),
                 VBox([name,save])])
tag_pars = interactive_output(plot_tagging,{'omega':omega,'d_omega':d_omega,'eff':eff,'d_eff':d_eff,
                                            'sigma_t':sigma_t,
                                            'a_acc':a_acc,'n_acc':n_acc,'b_acc':b_acc,'beta_acc':beta_acc,'cutoff_acc':cutoff_acc,
                                            'dm':dm,'dg':dg,'gs':gs,
                                            'r':r,'delta':delta,'gamma':gamma,'beta':beta,'k':k,
                                            'xmin':xmin,'xmax':xmax,'y_tag':y_tag,'y_untag':y_untag,'y_mix':y_mix,
                                            'k_acc':k_acc,'k_res':k_res,
                                            'name':name,'save':save,
                                            'b_f':b_f,
                                            'bbar_f':bbar_f,
                                            'bbar_fbar':bbar_fbar,
                                            'b_fbar':b_fbar,
                                            'fold_amix':fold_amix})
