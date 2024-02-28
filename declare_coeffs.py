import ipywidgets as widgets
from ipywidgets import interact, interactive, interactive_output
from ipywidgets import Layout, Button, Box, VBox, HBox
from plot_coeffs import plot_coeffs
from declare_dec import dm, dg, gs, r, delta, gamma, beta, k
from declare_acc import a_acc, n_acc, b_acc, beta_acc, cutoff_acc
from declare_res import sigma_t
from declare_ft import omega, d_omega, eff, d_eff
from declare_asym import a_prod, a_det

# select
b_f = widgets.Checkbox(value=True,description=r'$B$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
bbar_f = widgets.Checkbox(value=False,description=r'$\overline{B}$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
bbar_fbar = widgets.Checkbox(value=False,description=r'$\overline{B}$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
b_fbar = widgets.Checkbox(value=False,description=r'$B$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
u_f = widgets.Checkbox(value=False,description=r'$U$$\to$$f$',disabled=False,layout=widgets.Layout(width='200px'))
u_fbar = widgets.Checkbox(value=False,description=r'$U$$\to$$\overline{f}$',disabled=False,layout=widgets.Layout(width='200px'))
# select
k_dec = widgets.Checkbox(value=True,description=r'Decay',disabled=False,layout=widgets.Layout(width='200px'))
k_acc= widgets.Checkbox(value=False,description=r'Acceptance',disabled=False,layout=widgets.Layout(width='200px'))
k_res= widgets.Checkbox(value=False,description=r'Resolution',disabled=False,layout=widgets.Layout(width='200px'))
k_tag= widgets.Checkbox(value=False,description=r'Tagging',disabled=False,layout=widgets.Layout(width='200px'))
k_asymm= widgets.Checkbox(value=False,description=r'Asymmetries',disabled=False,layout=widgets.Layout(width='200px'))
## decay rate coefficients
xmin=widgets.BoundedFloatText(value=0, min=0, max=20, step=1, continuous_update=False, description=r'$t_{min}$ [ps]',layout=widgets.Layout(width='200px'))
xmax=widgets.BoundedFloatText(value=5, min=0, max=20, step=1, continuous_update=False, description=r'$t_{max}$ [ps]',layout=widgets.Layout(width='200px'))
y_cosh=widgets.BoundedFloatText(value=1, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{\cosh}$ [a.u.]',layout=widgets.Layout(width='200px'))
y_sinh=widgets.BoundedFloatText(value=0.02, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{\sinh}$ [a.u.]',layout=widgets.Layout(width='200px'))
y_cos=widgets.BoundedFloatText(value=1, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{\cos}$ [a.u.]',layout=widgets.Layout(width='200px'))
y_sin=widgets.BoundedFloatText(value=1, min=0, max=10, step=0.1, continuous_update=False, description=r'$y_{\sin}$ [a.u.]',layout=widgets.Layout(width='200px'))
name=widgets.Text(value='plots/coeffs.eps',continuous_update=False,description='Save as:',layout=widgets.Layout(width='200px'))
save=widgets.ToggleButton(value=False,description='Save',layout=widgets.Layout(width='200px'))

## Decay Rate Coefficients
wbox_coeffs = HBox([VBox([xmin,xmax,y_cosh,y_sinh,y_cos,y_sin]),
                    VBox([k_dec,k_acc,k_res,k_tag,k_asymm]),
                    VBox([b_f,bbar_f,bbar_fbar,b_fbar,u_f,u_fbar]),
                    VBox([name,save])
                    ])
coeffs_pars = interactive_output(plot_coeffs,{
                'dm':dm,'dg':dg,'gs':gs,'r':r,'delta':delta,'gamma':gamma,'beta':beta,'k':k,
                'a_acc':a_acc,'n_acc':n_acc,'b_acc':b_acc,'beta_acc':beta_acc,'cutoff_acc':cutoff_acc,
                'sigma_t':sigma_t,'omega_tag':omega,'d_omega_tag':d_omega,'eff_tag':eff,'d_eff_tag':d_eff,
                'a_prod_asym':a_prod,'a_det_asym':a_det,
                'xmin':xmin,'xmax':xmax,'y_cosh':y_cosh,'y_sinh':y_sinh,'y_cos':y_cos,'y_sin':y_sin,
                'name':name,'save':save,
                'k_dec':k_dec,
                'k_acc':k_acc,
                'k_res':k_res,
                'k_tag':k_tag,
                'k_asymm':k_asymm,
                'b_f':b_f,
                'bbar_f':bbar_f,
                'bbar_fbar':bbar_fbar,
                'b_fbar':b_fbar,
                'u_f':u_f,
                'u_fbar':u_fbar})
